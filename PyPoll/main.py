# Pypoll main.py 
# JAP 06212021

import os
import csv
import operator
from collections import Counter
rows = []

csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        rows.append(row)

    #count the total number of votes cast
    votescast = len(rows)
    
    # Determine unique Candidates 
    Candidates = []
    for row in rows:
        Candidates.append(row[2])
    list = (Counter(Candidates))
    Winner = max(list.items(), key=operator.itemgetter(1))[0]
    
    # write to the console
    print(f'Election Results')
    print(f'------------------------------------')
    print(f"Total Votes: {votescast}")
    print(f'------------------------------------')
    for key in list:
        print(key, ':' , ('%.3f'%(int(list[key])/votescast*100)),'% (',list[key],')')
    print(f'------------------------------------')
    print(f"Winner: {Winner}")
    print(f'------------------------------------')
    
    #write to the csv file
    output_path = os.path.join("polls.text")
    with open(output_path, 'w', newline='') as f:
        f.writelines("Election Results \n")
        f.writelines('\n')
        f.writelines('-------------------------------------\n')
        f.writelines('\n')
        f.writelines(f"Total Votes: {votescast} \n")
        f.writelines('\n')
        f.writelines('------------------------------------\n')
        f.writelines('\n')
        for key in list:
            f.write(f"{key}:  {('%.3f'%(int(list[key])/votescast*100))}% ({list[key]})\n")
        f.writelines('\n')
        f.writelines('------------------------------------\n')
        f.writelines('\n')
        f.writelines(f"Winner: {Winner} \n")
        f.writelines('\n')
        f.writelines('------------------------------------\n')