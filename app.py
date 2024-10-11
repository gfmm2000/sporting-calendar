from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, send_file
import json
from datetime import datetime
from ics import Calendar, Event

load_dotenv()

def load_data(path='fixtures.json'):
    with open(path) as f:
        data = json.load(f)
    return data

def save_data(data, path='fixtures.json'):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)  


def sort_fixtures(fixtures):
    return sorted(fixtures, key=lambda x: (x['Date'], x['Time']))


data = load_data()
data = sort_fixtures(data)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/add_fixture', methods=['GET', 'POST'])
def add_fixture():
    global data

    if request.method == 'POST':
        # Handle form submission
        opponent = request.form.get('opponent')
        home_away = request.form.get('home_away')
        date = request.form.get('date')
        time = request.form.get('time')
        competition = request.form.get('competition')

        # Create a new fixture dictionary
        new_fixture = {
            "Opponent": opponent,
            "Home/Away": home_away,
            "Date": date,
            "Time": time,
            "Competition": competition
        }

        data.append(new_fixture)

        save_data(data)
        data = sort_fixtures(data)

        return redirect(url_for('index'))

    return render_template('add_fixture.html')


@app.route('/remove_fixture/<int:index>', methods=['POST'])
def remove_fixture(index):
    # Logic to remove the fixture from your data source
    # For example, if you're using a list:
    del data[index]  # Remove the fixture at the specified index
    return redirect(url_for('index'))  # Redirect to the view displaying fixtures


@app.route('/download_ics', methods=['GET'])
def download_ics():
    # Load the data from JSON file
    with open('fixtures.json') as f:
        data = json.load(f)

    # Create a new calendar
    calendar = Calendar()

    for fixture in data:
        # Create an event for each fixture
        event = Event()

        # Determine if it's Home or Away
        home_away = fixture['Home/Away']

        # Add '[H]' or '[A]' in the event title based on Home or Away
        title_prefix = "[H] " if home_away == "Home" else "[A] "
        event.name = f"{title_prefix}{fixture['Opponent']}"

        # Set event start datetime
        start_datetime = datetime.strptime(f"{fixture['Date']} {fixture['Time']}", "%Y-%m-%d %H:%M")
        event.begin = start_datetime

        # Set event location (home stadium or placeholder for away)
        if home_away == "Home":
            event.location = "Estádio José Alvalade, Lisbon, Portugal"
        else:
            event.location = "Away game location - TBD"

        # Set event description as the competition
        event.description = fixture['Competition']

        # Add the event to the calendar
        calendar.events.add(event)

    # Save the calendar to an .ics file
    ics_file_path = 'fixtures.ics'
    with open(ics_file_path, 'w') as f:
        f.writelines(calendar)

    # Send the .ics file as a downloadable attachment
    return send_file(ics_file_path, as_attachment=True, download_name='fixtures.ics')

if __name__ == "__main__":
    app.run(debug=True)




# @app.route('/edit_fixture/<int:index>', methods=['GET', 'POST'])
# def edit_fixture(index):
#     global data  # Declare 'data' as a global variable

#     if request.method == 'POST':
#         # Handle form submission to update the fixture
#         opponent = request.form.get('opponent')
#         home_away = request.form.get('home_away')
#         date = request.form.get('date')
#         time = request.form.get('time')
#         competition = request.form.get('competition')

#         # Update the fixture data
#         data[index] = {
#             "Opponent": opponent,
#             "Home/Away": home_away,
#             "Date": date,
#             "Time": time,
#             "Competition": competition
#         }

#         # Save the updated data back to the JSON file
#         save_data(data)

#         # Redirect back to the index page after processing
#         return redirect(url_for('index'))

#     # Render the edit fixture form
#     fixture = data[index]  # Get the fixture to edit
#     return render_template('edit_fixture.html', fixture=fixture, index=index)
