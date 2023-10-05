import os
import csv

election_csv = os.path.join(r"C:\Users\Michael Krebs\Desktop\Data Analysis Course\Module 3 Challenge\python_challenge\PyPoll\Resources\election_data.csv")

#Open csv file
with open(election_csv) as csvfile:

        #Lists to store data
        candidates = []
        candidate_votes = {}
                
        #Vote counter
        votes = 0

        #Variable to hold contents
        csvreader = csv.reader(csvfile)

        #Reader header as the first row
        csv_header = next(csvreader)
        print(f"CSV Header: {csv_header}")

        #Read rows after the header
        for row in csvreader:
                
                #Total Votes
                votes = votes + 1

                #Candidates
                candidates.append(str(row[2]))
                              
                




print("Election Results")
print("----------------------------------------")
print("Total Votes:", len(votes))
print("----------------------------------------")
#print("Charles Casper Stockham: ", )
#print("Diana DeGette: " + " " + " " "\n")
#print("Raymon Anthony Doane: " + " " + " " "\n")
#print("----------------------------------------" "\n")
#print("Winner: " + " " "\n")
#print("----------------------------------------" "\n")