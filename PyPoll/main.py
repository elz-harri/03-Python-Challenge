# Import the OS module: This allows us to create file paths across operating systems
import os

# Module for opening & reading CSV files
import csv

#Determine working directory
csvpath=os.path.join(r"C:\Users\eliza\Desktop\Data Analytics\Git Hub Repositories\03-Python-Challenge\PyPoll\Resources\election_data.csv")

with open(csvpath, newline='') as csvfile:

# Tell Python how to read the info from the file
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
# Create lists to store data
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

# Determine votes, counties & candidates in the data set:
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

# Find the total votes cast:
    total_votes = (len(votes))
   
# Determine the votes per candidate:
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    
    
 # Determine the percentage of votes each candidate won
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 2)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 2)
    
# The winner of the election
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

        #Print Statements

print(f'Election Results')
print(f'-----------------------------------')
print(f'Total Votes: {total_votes}')
print(f'-----------------------------------')
print(f'Khan: {khan_percent}% ({khan_votes})')
print(f'Correy: {correy_percent}% ({correy_votes})')
print(f'Li: {li_percent}% ({li_votes})')
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
print(f'-----------------------------------')
print(f'Winner: {winner}')
print(f'-----------------------------------')


# Print/Export the following information into a text file:
output_path = os.path.join(r"C:\Users\eliza\Desktop\Data Analytics\Git Hub Repositories\03-Python-Challenge\PyPoll\Analysis\poll_analysis.txt")
with open(output_path, 'w') as outputHeader:
    outputHeader.write(f'-----------------------------------')
    outputHeader.write('\n')
    outputHeader.write(f'Election Results')
    outputHeader.write('\n')
    outputHeader.write(f'-----------------------------------')
    outputHeader.write('\n')
    outputHeader.write(f'Total Votes: {total_votes}')
    outputHeader.write('\n')
    outputHeader.write(f'-----------------------------------')
    outputHeader.write('\n')
    outputHeader.write(f'Khan: {khan_percent}% ({khan_votes})')
    outputHeader.write('\n')
    outputHeader.write(f'Correy: {correy_percent}% ({correy_votes})')
    outputHeader.write('\n')
    outputHeader.write(f'Li: {li_percent}% ({li_votes})')
    outputHeader.write('\n')
    outputHeader.write(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
    outputHeader.write('\n')
    outputHeader.write(f'-----------------------------------')
    outputHeader.write('\n')
    outputHeader.write(f'Winner: {winner}')
    outputHeader.write('\n')
    outputHeader.write(f'-----------------------------------')
    