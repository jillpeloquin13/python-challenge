# PyBank main.py
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset
# he net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

import os
import csv

#get the path, remember that this is with respect to where the python script is found 
csvpath = os.path.join('Resource', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #count/define the number of months
    months = len(list(csvreader))
    print(months)
 
