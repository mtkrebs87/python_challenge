#import os
import csv

election_csv = (r"C:\Users\Michael Krebs\Desktop\Data Analysis Course\Module 3 Challenge\python_challenge\PyPoll\Resources\election_data.csv")

#Lists to store data
candidate_list = {}
                
#Vote counter
total_votes = 0

#Value for candidate
candidate = "c"

#Winner vote counter and name
winner_votes = 0
winner = "w"

#Open csv file
with open(election_csv) as csvfile:

        #Variable to hold contents
        csvreader = csv.reader(csvfile)

        #Reader header as the first row
        csv_header = next(csvreader)
        #print(f"CSV Header: {csv_header}")

        #Read rows after the header
        for row in csvreader:
                
                #Total Votes
                total_votes += 1

                #Candidates from list
                candidate = row[2]

                #Add candidates to list
                if candidate in candidate_list:

                        #Put candidate name in list
                        candidate_list[candidate] += 1
                else:
                        candidate_list[candidate] = 1

for candidate in candidate_list:

        #Calculate candidate's votes
        percentage = (candidate_list[candidate]/total_votes)*100

        if candidate_list[candidate] > winner_votes:
                winner_votes = candidate_list[candidate]
                winner = candidate
                

print("Election Results")
print("----------------------------------------")
print("Total Votes:", (total_votes))
print("----------------------------------------")
print("Charles Casper Stockham: ", str(percentage) + "%" + str(candidate_list[candidate]))
print("Diana DeGette: ", str(percentage) + "%" + str(candidate_list[candidate]))
print("Raymon Anthony Doane: ", str(percentage) + "%" + str(candidate_list[candidate]))
print("----------------------------------------")
print("Winner: " + str(winner))
print("----------------------------------------")



#print("Election Results")
#print("----------------------------------------" "\n")
#print("Total Votes:", (total_votes))
#print("----------------------------------------" "\n")
#print("Charles Casper Stockham: ", str(percentage) + "%" + str(candidate_list[candidate]), "\n")
#print("Diana DeGette: ", str(percentage) + "%" + str(candidate_list[candidate]), "\n")
#print("Raymon Anthony Doane: ", str(percentage) + "%" + str(candidate_list[candidate]), "\n")
#print("----------------------------------------" "\n")
#print("Winner: " + str(winner))
#print("----------------------------------------" "\n")
