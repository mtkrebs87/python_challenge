
#Import csv file
import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")
output_folder = os.path.join("analysis", "Election Results.txt")

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
        percentage = ((candidate_list[candidate])/total_votes)*100
        percent_votes = "{:.3f}".format(percentage)

        if candidate_list[candidate] > winner_votes:
                winner_votes = candidate_list[candidate]
                winner = candidate
                

print("Election Results")
print("----------------------------------------")
print("Total Votes:", (total_votes))
print("----------------------------------------")
print("Charles Casper Stockham: ", str(percent_votes) + "%" + " " + str(candidate_list[candidate]))
print("Diana DeGette: ", str(percent_votes) + "%" + " " + str(candidate_list[candidate]))
print("Raymon Anthony Doane: ", str(percent_votes) + "%" + " " + str(candidate_list[candidate]))
print("----------------------------------------")
print("Winner: " + str(winner))
print("----------------------------------------")


with open(output_folder, "w") as text:

        text.write("Election Results" "\n")
        text.write("----------------------------------------" "\n")
        text.write("Total Votes:" + str(total_votes) + "\n")
        text.write("----------------------------------------" "\n")
        text.write("Charles Casper Stockham: " + str(percent_votes) + "%" + " " + str(candidate_list[candidate]) + "\n")
        text.write("Diana DeGette: " + str(percent_votes) + "%" + " " + str(candidate_list[candidate]) + "\n")
        text.write("Raymon Anthony Doane: " + str(percent_votes) + "%" + " " + str(candidate_list[candidate]) + "\n")
        text.write("----------------------------------------" + "\n")
        text.write("Winner: " + str(winner) + "\n")
        text.write("----------------------------------------" + "\n")