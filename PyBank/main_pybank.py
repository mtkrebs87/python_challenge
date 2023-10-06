
#Import csv file
import os
import csv

#budget_csv = os.path.join("..", "Resources", "budget_data.csv")
budget_csv = (r"C:\Users\Michael Krebs\Desktop\Data Analysis Course\Module 3 Challenge\python_challenge\PyBank\Resources\budget_data.csv")

#Open csv file
with open(budget_csv) as csvfile:

    #List to store data
    profit_loss_change = []
    monthly_change = []
    date = []
    total_profit_loss = []

    #specify variable to hold contents
    csvreader = csv.reader(csvfile)
 
    #Reader header as the first row
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #Read rows after header
    for row in csvreader:

        #Total months
        date.append(row[0])
        
        #Total profit/losses
        total_profit_loss.append(int(row[1]))

        #Add monthly change list for increase/decrease of profits
        monthly_change.append(row[1])

    #Changes in Profit and Loss            
    for numbers in range(len(monthly_change)-1):
        profit_loss_change.append(total_profit_loss[numbers + 1] - total_profit_loss[numbers])
    
        #Greatest Increase of Profits
        increase = max(profit_loss_change)

        #Greatest Decrease of Profits
        decrease = min(profit_loss_change)

        #Month with greatest increase of profits
        month_increase = profit_loss_change.index(max(profit_loss_change)) + 1

        #Month with greatest decrease of profits
        month_decrease = profit_loss_change.index(min(profit_loss_change)) + 1

        #Average Change
        average_change = ((sum(total_profit_loss)) / (len(date)))
        
    
#Work on calculating the correct total and averages in addition to lists for date and increase/decrease profits

print("Financial Analysis")
print("--------------------------------")
print("Total Months: ", len(date))
print("Total: ", "$", sum(total_profit_loss))
print("Average Change: ", str((round(int(average_change)),2)))
print("Greatest Increase in Profits: ", date[month_increase], "$", str(increase) )
print("Greatest Decrease in Profits: ", date[month_decrease], "$", str(decrease) )

#Don't forget to add "\n" to start new line at the end of each line of code


with open("Financial Analysis", "w") as text:

    text.write("Financial Analysis" + "\n")
    text.write("--------------------------------" + "\n")
    text.write("Total Months: " + str(len(date)) + "\n")
    text.write("Total: " + str(sum(total_profit_loss)) + "\n")
    text.write("Average Change: " + str(average_change) + "\n")
    text.write("Greatest Increase in Profits: " + str(date[month_increase]) + "$" + str(increase) + "\n")
    text.write("Greatest Decrease in Profits: " + str(date[month_decrease]) + str(decrease) + "\n")