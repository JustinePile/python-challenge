import os, csv
months, profit = 0, 0

# Path to data
budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None) # Move past header row

    # Count rows to determine how many months there are
    for row in csvreader:
        months += 1
        profit += int(row[1])

        
results = f'''\n
Financial Analysis \n 
---------------------------- \n
Total Months: {str(months)} \n
Total: ${profit} \n
Average Change: \n
\n '''

print (results)