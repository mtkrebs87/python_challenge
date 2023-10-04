
#Import csv file
import csv

budget_csv = (r"C:\Users\Michael Krebs\Desktop\Data Analysis Course\Module 3 Challenge\python_challenge\PyBank\Resources\budget_data.csv")

#List to store data
p_l_change = []
monthly_change = []
date = []

#Variables
month_count = 0
total_p_l = 0
average_p_l = 0
first_profit = 0

#Open csv file
with open(budget_csv) as csvfile:

    #specify variable to hold contents
    csvreader = csv.reader(csvfile)
 
    #Reader header as the first row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Read rows after header
    for row in csvreader:

        #Total months
        month_count = month_count + 1
        
        #Total profit/losses
        total_p_l += int(row[1])

        #Add date to list for increase/decrease of profits
        date.append(row[0])
        
        #Profit and Loss changes (total)
        last_profit = (row[1])
        p_l_change = last_profit - first_profit

        #Add monthly change list for increase/decrease of profits
        monthly_change.append(row[1])
        
        #Average Change
        average_p_l = int(row[1]) 
    

        #Greatest Increase of Profits
        

        #Greatest Decrease of Profits
        
    
#Work on calculating the correct total and averages in addition to lists for date and increase/decrease profits

print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(month_count))
print("Total: " + str(total_p_l))
print("Average Change: " + str(average_p_l))
print("Greatest Increase in Profits: " )
print("Greatest Decrease in Profits: " )

#Don't forget to add "\n" to start new line at the end of each line of code

with open("Financial Analysis", "w") as text:
    text.write("Financial Analysis" + "\n")
    text.write("--------------------------------" + "\n")
    text.write("Total Months: " + str(month_count) + "\n")
    text.write("Total: " + str(total_p_l) + "\n")
    text.write("Average Change: " + str(average_p_l) + "\n")
    text.write("Greatest Increase in Profits: " + str(date) +  "\n")
    text.write("Greatest Decrease in Profits: " + str(date) + "\n")