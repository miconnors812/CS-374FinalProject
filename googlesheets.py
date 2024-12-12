# all by owen fazzini
# this code runs the output google sheet, which is kept updated based on the values returned by userfunctions
# the google sheet contains a database of workers, hours, and pay (think oracle)


from userfunctions import all_workers, hours, pay
from finalproject import generate_database
import gspread
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
import re 
import csv

# opens spreadsheet with the service account provided by key.json
gc = gspread.service_account("C:/Users/shado/testscripts/mongan final project/key.json")
wks = gc.open("final project output spreadsheet").sheet1
database = generate_database("C:/Users/shado/testscripts/mongan final project/finalproject.csv")

def update():
    workers = all_workers(database)
    # check to see if there's a corresponding cell for each worker,
    # and, if not, update the spreadsheet accordingly
    for i in range(len(workers)):
        # creates regex pattern for the name of each worker
        regx = re.compile(re.escape(workers[i]))
        # searches sheet for matching patterns
        matches = wks.findall(regx)
        # if the list of matches is empty,
        if len(matches) == 0:
            # add a cell with the worker's name
            wks.update_cell((i+2), 1, f'{workers[i]}')
    
    # now, add their pay rate
    # values will depend on this dictionary
    paydict = {
        "Worker": 15,
        "Manager": 30,
        "CEO": 45
    }
    
    # fetches the corresponding job for each worker
    with open("C:/Users/shado/testscripts/mongan final project/finalproject.csv") as csvfile:
         # reads the csv file into a list of lists
        reader = csv.reader(csvfile)
        rows = list(reader)

    truerows = []    
    # check to make sure we're not getting the info from a worker
    # who's already in the system. if you have the same name as someone else,
    # oh well.
    for i in range(1,len(rows)):
        if all(row[2] != rows[i][2] for row in truerows):
            truerows.append(rows[i])

    # update job title, time, and pay
    for i in range(len(truerows)):
        row = (truerows[i][1])
        wks.update_cell(i+2, 2, f'${paydict[row]}/hr')
        time = (hours(workers[i], database) / 60)
        wks.update_cell(i+2, 3, f'{time}')
        wks.update_cell(i+2, 4, f'${pay(workers[i], database)}')



update()
