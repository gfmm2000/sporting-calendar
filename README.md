# Sporting CP Fixtures Project

This project provides an overview of the upcoming Sporting CP football fixtures. It includes an HTML file for displaying the matches and a CSV file for storing the fixture data. Additionally, there is a Python script that links the CSV and HTML files for further data manipulation and display.

## Project Structure

- `fixtures.csv`: A CSV file containing the upcoming Sporting CP fixtures with the following columns:
  - Opponent
  - Home/Away
  - Date
  - Time
  - Competition

- `sporting_cp_fixtures.html`: An HTML file that displays the Sporting CP fixtures in a table format.

- `link_files.py`: A Python script that:
  1. Loads the CSV file and prints the data.
  2. Provides a basic structure to extend the project, for example, using Flask to serve the HTML and dynamically update the fixtures.

## How to Use

1. **View Fixtures**: Open the `sporting_cp_fixtures.html` file in any web browser to view the list of upcoming Sporting CP fixtures.

2. **Work with Data**: Use the `link_files.py` Python script to load the CSV file and manipulate the data. This script can be extended to integrate the data with web applications or further analysis.

3. **Extend the Project**: The provided Python script can be used as a base for integrating the fixture data with a web server using frameworks like Flask or Django, or for exporting the data in different formats (e.g., JSON, XML).

## Requirements

- Python 3.x
- pandas (for handling CSV data)

## Example Usage

```bash
# Install pandas if you don't have it
pip install pandas

# Run the Python script to print the fixture data
python link_files.py
```

## License

This project is open-source and free to use.
