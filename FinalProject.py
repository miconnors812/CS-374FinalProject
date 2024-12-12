#                                   CS-374 Final Project: Michael Connors, Evan Tilton, Owen Fazzini
#======================================================================================================================================
# The goal of this program is to utilize google forms to take your input and parse the downloaded google forms responses.
# We would like it to be able to read from a .csv of an excel spreadsheet since that is where the form responses will be stored.
# =====================================================================================================================================

import re           # for regular expressions
import requests     # pip install requests
from UserFunctions import *


def generate_database(file_name):
    # Turn file into an array of each row in the excel spreadsheet
    file = open(file_name)
    data = file.read()
    responses = data.split("\n")
    #print(responses)

    # Split each row into an array of each column's token
    tokens = [0] * len(responses)
    for i in range(len(responses)):
        tokens[i] = responses[i].split(",")
    print(tokens)

    return tokens

def generate_tokens(line):
    tokens = []
    tokentypes = []

    patterns = ['pay', 'hours', r'workername=\w+ \w+']
    
    patterntypes = ["pay", "hours", "workername"]

    i = 0
    for pattern in patterns:
        matches = re.findall(pattern, line)
        for match in matches:
            tokens.append(match)
            tokentypes.append(patterntypes[i])
        i += 1
    
    return tokens, tokentypes


def download_google_sheet_as_csv(sheet_id, file_name):
    # URL to export Google Sheets as CSV
    url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv'
    
    # Send GET request to download the CSV
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print(f"CSV file downloaded as {file_name}")
    else:
        print(f"Failed to download the file. HTTP status code: {response.status_code}")



sheet_id = '1l20PqkNbb3_HmhJprtnLzuWiBWeYkbv6t5RQKZKMtGU'  #<------ Put Sheet ID in the URL here
file_name = 'FinalProject.csv'
download_google_sheet_as_csv(sheet_id, file_name)
database = generate_database(file_name)

line = "hi" # change line to be user input of command
tokens = generate_tokens(line)

pay("all",database)

