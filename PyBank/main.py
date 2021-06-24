# PyBank main.py
# JAP 06212021

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
    
    #count the total value in row[1]
    numbertotal = 0.0
    for row in rows:
        numbertotal += float(row[1])

    # create a new list that subtracts the previous value to calculate the difference
    previous = 0
    for row in rows:
        value1 = float(row[1])
        ave = value1-previous
        values = [row[0], ave]
        ave_change.append(values)
        previous = value1
    
    #get rid of the first row as not valid and create the sum to use for averages, min and max changes
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

    #define Average Change and then greatest/least variables for easy printing
    AverageChange = sum/(months-1)
    GIPM = TotalIncrease[0]
    GIPV = TotalIncrease[1]
    LIPM = TotalDecrease[0]
    LIPV = TotalDecrease[1]

    #print the analysis to the console
    print("Financial Analysis")
    print('--------------------------------')
    print(f"Total Months: {months}")
    print(f"Total ${numbertotal}")
    print(f"Average Change: ${sum/(months-1):5.2f}")
    print(f"Greatest Increase in Profits: {GIPM} ($ {GIPV})")
    print(f"Greatest Decrease in Profits: {LIPM} ($ {LIPV})")

output_path = os.path.join("financials.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Total Months", "Total Net", "Average Change", "Greatest Increase in Profits Month", "Greatest Increase in Profits Money", "Greatest Decrease in Profits Month", "Greatest Decrase in Profits Money"])
    csvwriter.writerow([months, numbertotal, AverageChange, GIPM, GIPV, LIPM, LIPV])


output_path = os.path.join("financials.text")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as f:
    f.writelines("Financial Analysis \n")
    f.writelines('\n')
    f.writelines('-------------------------------- \n')
    f.writelines('\n')
    f.writelines(f"Total Months: {months} \n")
    f.writelines(f"Total ${numbertotal} \n")
    f.writelines(f"Average Change: ${sum/(months-1):5.2f} \n")
    f.writelines(f"Greatest Increase in Profits: {GIPM} ($ {GIPV}) \n")
    f.writelines(f"Greatest Decrease in Profits: {LIPM} ($ {LIPV}) \n")