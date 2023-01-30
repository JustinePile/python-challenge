# Python scripts to analyze records

## PyBank calculates:
* The total number of months included in the dataset
* The net total amount of "Profit/Losses" over the entire period
* The changes in "Profit/Losses" over the entire period, and then the average of those changes
* The greatest increase in profits (date and amount) over the entire period
* The greatest decrease in profits (date and amount) over the entire period

## PyPoll calculates:
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote

*PyBank and PyPoll each have thier own directory with a python script, a Resources directory that has the CSV data, and an analysis directory that contains that a text file with the scripts results*

### Directory structure
PyBank/  
├─ main.py  
├─ Resources/  
│  ├─ budget_data.csv  
├─ analysis/  
│  ├─ PyBank.txt  
PyPoll/  
├─ main.py  
├─ analysis/  
│  ├─ PyPoll.txt  
├─ Resources/  
│  ├─ election_data.csv  

![Screenshot](https://i.imgur.com/y9Bmgsb.png)
