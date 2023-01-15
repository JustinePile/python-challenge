import os, csv

votes = 0
ballot_ID, candidate, candidates = [], [], []
num_votes = {}
pct = [0, 0, 0]

# Path to data
election_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None) #Move past header row

    # Iterate through file
    for row in csvreader:
        votes += 1 # Count rows to determine how many votes there are
        candidate.append(row[2]) # Add candidates to list

# Find all unique candidates
for name in candidate:
    if name not in candidates: 
        candidates.append(name)

# Count candidates and vote counts
for cnt in candidate:
    if cnt not in num_votes:
        num_votes[cnt] = 0
    num_votes[cnt] = num_votes[cnt] + 1
vote_count = list(num_votes.values()) # Take dictionary values for vote count and put them in a list

# Calc vote %s
for x in range(len(vote_count)):
    pct[x] = round(((vote_count[x] / votes) * 100), 3)

# Find election winner
max_value = max(vote_count)
max_index = vote_count.index(max_value)
winner = candidates[max_index]

# Assigns results to a variable
results = f'''Election Results \n 
---------------------------- \n
Total Votes: {votes} \n
------------------------- \n
{candidates[0]}: {pct[0]}% ({vote_count[0]}) \n
{candidates[1]}: {pct[1]}% ({vote_count[1]}) \n
{candidates[2]}: {pct[2]}% ({vote_count[2]}) \n
------------------------- \n
Winner: {winner}\n
------------------------- \n
\n '''

# Prints results to terminal
print("\n" + results)

# Output results to file
with open("analysis\PyPoll.txt", "w") as output:
    output.write(results)