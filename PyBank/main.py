import os, csv
months, profit, avg = 0, 0, 0
changes, list, date = [], [], []

# Path to data
budget_csv = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None) # Move past header row

    # Iterate through file
    for row in csvreader:
        months += 1     # Count rows to determine how many months there are
        profit += int(row[1])   # Calc the sum of profit column
        changes.append(int(row[1]))     # Create a list with all data from profit/losses column to calc avg change (later)
        date.append(str(row[0]))     # Create a list with all data from date column

# Calculate the average change for the profit column 
for x in range(months-1):
    avg = avg - changes[x] + changes[x+1]
    list.append(changes[x+1] - changes[x])

# Get the highest and lowest values from list which contains all the change values
highest = max(list)
lowest = min(list)

# Find index positions of the max and min values
max_index = list.index(highest) + 1  #  Add 1 to offset 0 based indexing
min_index = list.index(lowest) + 1
max_date = date[max_index]  # Find the associated dates based on the index positions
min_date = date[min_index]  

# Calc the avg of the changes
avg = avg / (months-1)       
avg = round(avg, 2)

# Assigns results to a variable
results = f'''Financial Analysis \n 
---------------------------- \n
Total Months: {str(months)} \n
Total: ${profit} \n
Average Change: ${avg} \n
Greatest Increase in Profits: {max_date} (${highest}) \n
Greatest Decrease in Profits: {min_date} (${lowest}) \n
\n '''

# Prints results to terminal
print("\n" + results)

# Output results to file
with open("analysis\PyBank.txt", "w") as output:
    output.write(results)
