"""
Kyle Finley Homework 3 ITIN 8000
Part 2

In part 2 you will download data from Kaggle.com and pull information from a CSV and then process it and export the result as a JSON file.
Please:

Download the FiveThirtyEight Comic Characters (Links to an external site.) dataset
Extract the CSV and place it in your project directory for the assignment
Create a file named hw3part2.py that does the following
Imports the data from dc-wikia-data.csv and marvel-wikia-data.csv

Combines them into a single JSON file called ComicCharacters.JSON
The JSON file should list every character as an object by "Character Name"
Must Contain Object Ownership containing the value Publisher (DC or Marvel)
Must contain the object Characteristics containing the values:
Alignment (Good, Bad, or Neutral)
Eye Color
Hair Color
Gender
When run it should generate a new file
"""

import csv
import json

jsonArray = []

# -----Imports the data from dc-wikia-data.csv and marvel-wikia-data.csv-----
with open('dc-wikia-data.csv', 'r') as csvf:
    # load csv file data using csv library's dictionary reader
    reader = csv.DictReader(csvf)
    # convert each csv row into python dict
    for row in reader:
        # add this python dict to json array
        jsonArray.append(row)

    with open('marvel-wikia-data.csv', 'r') as csvf:
        # load csv file data using csv library's dictionary reader
        reader = csv.DictReader(csvf)
        # convert each csv row into python dict
        for row in reader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
        with open('jsonFilePath2', 'w', encoding='utf-8') as jsonf:
            jsonString = json.dumps(jsonArray, indent=4)
            jsonf.write(jsonString)


#Combines them into a single JSON file called ComicCharacters.JSON
#The JSON file should list every character as an object by "Character Name"
# Must Contain Object Ownership containing the value Publisher (DC or Marvel)
# Must contain the object Characteristics containing the values:
# Alignment (Good, Bad, or Neutral)
# Eye Color
# Hair Color
# Gender
# When run it should generate a new file




