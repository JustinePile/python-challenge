import os, csv
months, profit, avg = 0, 0, 0
changes = []

# Path to data
budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None) # Move past header row

    #Iterate through file
    for row in csvreader:
        months += 1     # Count rows to determine how many months there are
        profit += int(row[1])   # Calc the sum of profit column
        changes.append(int(row[1]))     # Create a list with all data from column 2

# Calculate the average change for the profit column 
for x in range(months-1):
   avg = avg - changes[x] + changes[x+1]
avg = avg / (months-1)       
avg = round(avg, 2)

# Assigns results to a variable
results = f'''\n
Financial Analysis \n 
---------------------------- \n
Total Months: {str(months)} \n
Total: ${profit} \n
Average Change: ${avg} \n
\n '''

# Prints results to terminal
print(results)