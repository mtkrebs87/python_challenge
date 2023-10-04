import os
import csv

election_csv = os.path.join(r"C:\Users\Michael Krebs\Desktop\Data Analysis Course\Module 3 Challenge\python_challenge\PyPoll\Resources\election_data.csv")
print(election_csv)



#Open csv file
with open(election_csv) as election_csv:

        #Variable to hold contents
        csv_reader = csv.reader(election_csv)

        #Reader header as the first row
        csv_header = next(csv_reader)
        print(f"CSV Header: {csv_header}")

        #Read rows after the header
        for row in csv_reader:
                total_votes = int(row[0])
                print(total_votes)
         




#print("Election Results" "\n")
#print("----------------------------------------" "\n")
#print("Total Votes:" "\n")
#print("----------------------------------------" "\n")
#print("Charles Casper Stockham: " + " " + " " "\n")
#print("Diana DeGette: " + " " + " " "\n")
#print("Raymon Anthony Doane: " + " " + " " "\n")
#print("----------------------------------------" "\n")
#print("Winner: " + " " "\n")
#print("----------------------------------------" "\n")