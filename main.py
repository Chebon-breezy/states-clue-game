from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load data from CSV file
data = pd.read_csv('states.csv')

# Define a function to check clues against the data


def check_clues(clues):
    # Convert user input to uppercase for case-insensitive matching
    clues = clues.upper()
    # Search for matches in both the state name and the clue column
    matches = data[(data['state'].str.upper() == clues) |
                   (data['clue'].str.upper() == clues)]
    return matches

# Define a route for the home page


@app.route('/')
def home():
    return render_template('index.html')

# Define a route for the search results page


@app.route('/search', methods=['POST'])
def search():
    # Get the user input from the form
    clues = request.form['clues']
    # Call the check_clues function to search for matches
    matches = check_clues(clues)
    # Render the search results template with the matches
    return render_template('results.html', matches=matches)


if __name__ == '__main__':
    app.run(debug=True)
