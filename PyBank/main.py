# PyBank main.py
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# he net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

import os
import csv
rows =[]
ave_change = []

#get the path, remember that this is with respect to where the python script is found 
csvpath = os.path.join('Resource', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        rows.append(row)
    
    
  
    #count/define the number of months
    months = len(rows)
    
    
    numbertotal = 0.0
    for row in rows:
        numbertotal += float(row[1])
    
    
    previous = 0
    for row in rows:
        value1 = float(row[1])
        ave = value1-previous
        values = [row[0], ave]
        ave_change.append(values)
        previous = value1
    
    #get rid of the first row as not valid
    ave_change = (ave_change[1:])
    
    sum = 0.0
    for row in ave_change:
        sum += float(row[1])
    
    


     # take the second element for sort
    def take_second(elem):
        return elem[1]

    # sort list with key
    sorted_list_ave = sorted(ave_change, key=take_second)
    TotalIncrease = sorted_list_ave[-1]
    TotalDecrease = sorted_list_ave[0]

    print(f"Financial Analysis")
    print("------------------------------------")
    print(f"Total Months: {months}")
    print(f"Total ${numbertotal}")
    print(f"Average Change: ${sum/(months-1):5.2f}")
    print(f"Greatest Increase in Profits:", TotalIncrease[0], "($",TotalIncrease[1],")")
    print(f"Greated Decrease in Profits:", TotalDecrease[0], "($",TotalDecrease[1],")")
