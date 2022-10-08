
from doctest import OutputChecker
import os
import csv

PROFIT_IDX = 1
#Name the file path with OS standardization
file_path = os.path.join('Resources', 'budget_data.csv')

#Read in CSVs using CSV Module
with open(file_path) as file:
    csvreader = csv.reader(file, delimiter=',')

#Pull out headers
    header = next(csvreader)
    
    total_profit = 0
    avg_change = 0
    num_months = 0
    sumchanges = 0
    old_profit = 0
    num_of_changes = 0
    first_row = True
    
    for row in (csvreader):
        num_months += 1
        profit = int(row[PROFIT_IDX])
        total_profit = total_profit + profit
        
        if not first_row:
            num_of_changes +=1
            change = profit - old_profit
            sumchanges = sumchanges + change

            if num_of_changes == 1:
                max_increase = change
                max_decrease = change
            if change > max_increase:
                max_increase = change
            if change < max_decrease:
                max_decrease = change
        
        old_profit = profit
        first_row = False
    
    avg_change = sumchanges / num_of_changes
#   print(header)
    print("Financial Analysis")
    print("___________________________________")
    print("Total Months: ")
    print(num_months)
    print("---------------------")
    print("Total Profit: ")
    print(total_profit)
    print("---------------------")
    print("Average Change: ")
    print(avg_change)
    print("---------------------")
    print("Max Increse: ")
    print(max_increase)
    print("---------------------")
    print("Max Decrease: ")
    print(max_decrease)

import csv
output_path = 'python_output.csv'
with open(output_path, 'w') as csvfile:
   csvwriter = csv.writer(csvfile)

   csvwriter.writerow(['Total Months:', 'Total Profit:', 'Average Change:', 'Max Increase:', 'Max Decrease:'])
   csvwriter.writerow([num_months, total_profit, avg_change, max_increase, max_decrease])

    
            

        
   
        












    

      



