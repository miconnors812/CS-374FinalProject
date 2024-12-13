# These are the functions that will run once identified by the parser as included in user input
# All of this is Michael Connors's work, as well as the generate_database() and download_google_sheet_as_csv() functions in main

import re           # for regular expressions
import math         # to round down hours when printing time worked

# Helper method to find out if a worker has inputted their information into the system
def worker_exists(worker,database):
    exists = 0 # 0 is the base case and means that the worker does not have an entry in the database
    #match = re.I(r"all", worker) # possibly use case-insensitive search?
    if (worker == "all"):   # check if the user inputted "all"
        exists = 2; # if "all" is inputted as the worker name, then there is a special case for the function to perform
    else: 
        # loop through all workers and see if any name matches the input
        for i in range(1,len(database)):       # go through each response, excluding the format example 
                if len(database[i]) <= 2:
                    continue
                if (worker == database[i][2]): # database[2] is the column that holds all worker names in the spreadsheet
                    exists = 1
    #print(exists)
    return exists

def all_workers(database):
    # "all" has been inputted, so add up every worker's hours.
    # However, there are duplicates for workers who inputted multiple times,
    # So we must also weed out those names that appear multiple times.
    workers = []
    for i in range(1,len(database)):

        # add safeguard to make sure we're not appending an empty list
        # (avoiding out of bounds errors)
        if len(database[i]) <= 2:
            continue

        workers.append(database[i][2])  # preemptively add their name to the end
        #print(database[i][2] + " appended!")
        for j in range(len(workers)-1):   # check every name but the most recent
            #print(workers[j]+" VS "+workers[len(workers)-1])
            if (workers[j] == workers[len(workers)-1]): # has this name already been put in the array of workers?
                workers.pop()                  # if so, remove them
                #print("Duplicate popped!")
                break                             # we don't need to go any further
    return workers


def pay(worker,database):
    earnings = 0
    wage = 0
    exists = worker_exists(worker,database)
    if (exists > 0): 
        if (exists == 1): # only one employee's name was inputted 

            # Determine Worker's job position
            job = ""
            for i in range(1,len(database)):
                if len(database[i]) < 3:
                        continue
                if (database[i][2] == worker) & (database[i][1] != job):
                    job = database[i][1]
            # <----------------- EDIT ANY PAY RATES HERE!!!!
            if (job == "Worker"):
                wage = 15        # $15 an hour for workers
            if (job == "Manager"):
                wage = 30        # $30 an hour for managers
            if (job == "CEO"):
                wage = 45        # $45 an hour for CEOs

            # Next, determine their hours
            time = hours(worker,database)

            # Finally, calculate their earnings
            earnings = time * wage

        else:
            # add up every worker's pay recursively
            workers = all_workers(database)

            for employee in workers:
                earnings += pay(employee,database) # add up everyone's pay


    else:
        print("Incorrect input! The employee you named does not exist.")
        earnings = -1

    #print("How much money", worker, "earned: $", earnings)
    return earnings


def hours(worker,database):
    time = 0
    exists = worker_exists(worker,database)
    if (exists > 0): 
        if (exists == 1): # only one employee's name was inputted 

            for i in range(1,len(database)):
                if len(database[i]) <= 2:
                    continue
                if (database[i][2] == worker):

                    # Tokenize time inputs in order to parse them
                    clockedIn = database[i][4].split(" ")
                    clockedOut = database[i][5].split(" ")

                    clockedIn[0] = clockedIn[0].split(":")
                    if (clockedIn[1] == "AM") & (clockedIn[0][0] == "12"): #convert to military time if midnight
                        clockedIn[0][0] = "0"
                    # convert the current time into minutes since midnight
                    minsArrived = int(clockedIn[0][0])*60 + int(clockedIn[0][1]) # seconds: + int(clockedIn[0][2]/60)
                    if (clockedIn[1] == "PM") & (clockedIn[0][0] != "12"): 
                        minsArrived += 720     # add 12 hours if the time is PM (unless noon)
                    #print("minutes at arrival: ", minsArrived)

                    clockedOut[0] = clockedOut[0].split(":")
                    if (clockedOut[1] == "AM") & (clockedOut[0][0] == "12"): #convert to military time if midnight
                        clockedOut[0][0] = "0"
                    # convert the current time into minutes since midnight
                    minsLeft = int(clockedOut[0][0])*60 + int(clockedOut[0][1]) # seconds: + int(clockedOut[0][2]/60)
                    if (clockedOut[1] == "PM") & (clockedOut[0][0] != "12"): 
                        minsLeft += 720         # add 12 hours if the time is PM (unless noon)
                    #print("minutes at departure: ", minsLeft)

                    if (clockedIn[1] == "PM") & (clockedOut[1] == "AM"): # when you work into the next day, the calculation is different
                        timeSpent = minsLeft + (24*60 - minsArrived)
                    else: 
                        timeSpent = abs(minsLeft - minsArrived)
                    #print("time spent: ", timeSpent)

                    #------------------------------------------------
                    # BREAK DURATION PARSING HERE
                    #------------------------------------------------

                    # Tokenize input for break duration so it can be parsed
                    tokenizedBreak = database[i][6].split(" ")
                    breakDuration = 0
                    pendingNum = 0

                    # Scan tokenized input and parse keywords
                    for i in range(len(tokenizedBreak)):
                        if (tokenizedBreak[i] == "hours") | (tokenizedBreak[i] == "hour"):
                            #print("hours detected!")
                            breakDuration += pendingNum * 60
                            pendingNum = 0
                        elif (tokenizedBreak[i] == "secs") | (tokenizedBreak[i] == "seconds"):  # it's really dystopian to track seconds used up on breaks...
                            breakDuration += pendingNum / 60
                            pendingNum = 0
                        elif (tokenizedBreak[i] == "mins") | (tokenizedBreak[i] == "minutes") | (tokenizedBreak[i] == "minute") | (tokenizedBreak[i] == "min"):
                            #print("mins detected!")
                            breakDuration += pendingNum
                            pendingNum = 0
                        elif (re.search(r'\d', tokenizedBreak[i])):
                            #print("digit detected: " + tokenizedBreak[i])
                            pendingNum = int(tokenizedBreak[i])
                    if (timeSpent > breakDuration): # Make sure time spent doesn't turn negative if there is an edge case
                        timeSpent -= breakDuration  # You were not working over break, so subtract that time from hours worked
                    else:
                        timeSpent = 0
                    
                    time += timeSpent
                    

        else:
            # add up every worker's hours recursively
            workers = all_workers(database)                    

            for employee in workers:
                time += hours(employee,database) # add up everyone's pay


    else:
        print("Incorrect input! The employee you named does not exist.")
        time = -1
    #print("total minutes worked:",time)

    # statement to print out how much time that employee has spent working:
    #print("How long", worker, "spent working:", math.floor(time/60), "hours and", time%60, "minutes") # time%360 for seconds?
    return time

 
