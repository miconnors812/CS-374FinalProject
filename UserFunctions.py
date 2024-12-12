# These are the functions that will run once identified by the parser as included in user input
# All of this is Michael Connors's work, as well as the generate_database() and download_google_sheet_as_csv() functions in main

import re           # for regular expressions

# Helper method to find out if a worker has inputted their information into the system
def worker_exists(worker,database):
    exists = 0 # 0 is the base case and means that the worker does not have an entry in the database
    match = re.i("all", worker) # check if the user inputted "all" case insensitively
    if match == None:
        for i in range(1,len(database[2])):
            if (worker == database[2][i]):
                exists = 1
    else:
        exists = 2; # if "all" is inputted as the worker name, then there is a special case for the function
    return exists


def pay(worker,database):
    earnings = 0
    wage = 0
    exists = worker_exists(worker,database)
    if (exists > 0): 
        if (exists == 1): # only one employee's name was inputted 

            # Determine Worker's job position
            job = ""
            for i in range(1,len(database)):
                if (database[i][2] == worker & database[i][1] != job):
                    job = database[i][1]
            if (job == "Worker"):
                wage = 15        # $15 an hour for workers
            if (job == "Manager"):
                wage = 30        # $30 an hour for managers
            if (job == "CEO"):
                wage = 45        # $45 an hour for CEOs

            # Next, determine their hours
            #time = hours(worker,database)
            time = 5

            # Finally, calculate their earnings
            earnings = time * wage

        else:
            # "all" has been inputted, so add up every worker's pay.
            workers = [database[2]] # every worker
            # However, that includes duplicates for workers who inputted multiple times,
            # So we must weed out those names that appear multiple times.
            for i in range(1,len(workers)):
                for j in range(1,len(workers)):
                    if (workers[i] == workers[j]):
                        workers = workers[i:] + workers[:j+1]
            print(workers)
                    #if (database[2][i] == database[2][j]):


    else:
        print("Incorrect input! The employee you named does not exist.")
    return earnings


#def hours(worker,database):
    
#def compare(worker,toCompare,database):

#def 
