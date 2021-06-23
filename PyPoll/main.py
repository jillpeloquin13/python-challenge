# Pypoll main.py 
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

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
    
    # Determine unique Canididates 
    Candidates = []
    for row in rows:
        Candidates.append(row[2])
    list = (Counter(Candidates))
    Winner = max(list.items(), key=operator.itemgetter(1))[0]

    print(f'Election Results')
    print(f'------------------------------------')
    print(f"Total Votes: {votescast}")
    print(f'------------------------------------')
    for key in list:
        print(key, ':' , ('%.3f'%(int(list[key])/votescast*100)),'% (',list[key],')')
    print(f'------------------------------------')
    print(f"Winner: {Winner}")
    print(f'------------------------------------')
    
    
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