
from doctest import OutputChecker
from email.headerregistry import ContentTransferEncodingHeader
import os
import csv

#Name the file path with OS standardization
file_path = os.path.join('Resources', 'election_data.csv')

#Read in CSVs using CSV Module
with open(file_path) as file:
    csvreader = csv.reader(file, delimiter=',')

#Pull out headers
    header = next(csvreader)
    
    total_votes = 0
    candidates = []
    can_vote_perc = 0
    can_vote_total = 0
    prev_vote = 0
    next_row = []
    current_row = []

    for row in (csvreader):
        total_votes += 1
        next_row = row[2]
        if str(current_row) != str(next_row):
            candidates = current_row
    print(total_votes)
    print(candidates)
#   print candidates
        
        # print(candidates)

# import csv
# output_path = 'python_output.csv'
# with open(output_path, 'w') as csvfile:
#    csvwriter = csv.writer(csvfile)

#    csvwriter.writerow(['Total Months:', 'Total Profit:', 'Average Change:', 'Max Increase:', 'Max Decrease:'])
#    csvwriter.writerow([num_months, total_profit, avg_change, max_increase, max_decrease])
