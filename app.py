import os
from dotenv import load_dotenv
from flask import Flask, render_template
import pandas as pd

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():

    df = pd.read_csv('fixtures.csv')  
    data = df.to_dict(orient='records')
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
