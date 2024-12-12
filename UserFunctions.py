# These are the functions that will run once identified by the parser as included in user input
# All of this is Michael Connors's work, as well as the generate_database() and download_google_sheet_as_csv() functions in main

import re           # for regular expressions

# Helper method to find out if a worker has inputted their information into the system
def worker_exists(worker,database):
    exists = 0 # 0 is the base case and means that the worker does not have an entry in the database
    #match = re.I(r"all", worker) # possibly use case-insensitive search?
    if (worker == "all"):   # check if the user inputted "all"
        exists = 2; # if "all" is inputted as the worker name, then there is a special case for the function to perform
    else: 
        # loop through all workers and see if any name matches the input
        for i in range(1,len(database)):       # go through each response, excluding the format example 
                print(i)
                if (worker == database[i][2]): # database[2] is the column that holds all worker names in the spreadsheet
                    exists = 1
    #print(exists)
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
                if (database[i][2] == worker) & (database[i][1] != job):
                    job = database[i][1]
            if (job == "Worker"):
                wage = 15        # $15 an hour for workers
            if (job == "Manager"):
                wage = 30        # $30 an hour for managers
            if (job == "CEO"):
                wage = 45        # $45 an hour for CEOs

            # Next, determine their hours
            #time = hours(worker,database)
            
            time = 5 #TEST VALUEEE

            # Finally, calculate their earnings
            earnings = time * wage

        else:
            # "all" has been inputted, so add up every worker's pay.
            # However, that includes duplicates for workers who inputted multiple times,
            # So we must also weed out those names that appear multiple times.
            workers = []
            for i in range(1,len(database)):
                workers.append(database[i][2])  # preemptively add their name to the end
                for j in range(len(workers)-1):   # check every name but the most recent
                    if (workers[j] == workers[-1]): # has this name already been put in the array of workers?
                        workers.pop()                  # if so, remove them

            print(workers)
                    #if (database[2][i] == database[2][j]):


    else:
        print("Incorrect input! The employee you named does not exist.")
    return earnings


#def hours(worker,database):
    
#def compare(worker,toCompare,database):

#def 
