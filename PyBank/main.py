# Import the OS module: This allows us to create file paths across operating systems
import os

# Module for opening & reading CSV files
import csv

#Determine working directory

csvpath = os.path.join(r"C:\Users\eliza\Desktop\Data Analytics\Git Hub Repositories\03-Python-Challenge\PyBank\Resources\budget_data.csv")

with open(csvpath, 'r') as csvfile:
    
# Tell Python how to read the info from the file
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

 # Create lists to store data
    month = []
    revenue = []
    rev_change = []
    month_change = []
    
# Determine how many months are in the data set:       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
 

 # Find the total revenue 
    revenue_int = map(int,revenue)
    total_rev = (sum(revenue_int))
    

 # Find the average change
    i = 0
    for i in range(len(revenue) - 1):
        loss = int(revenue[i+1]) - int(revenue[i])

 # Append profit loss
        rev_change.append(loss)
    Total = sum(rev_change)

 # Print revenue change:
    month_change = Total / len(rev_change)
            
# Determine the greatest profit increase:
    increase = max(rev_change)
    k = rev_change.index(increase)
    monthly_increase = month[k+1]
    
# Determine the greatest profit decrease:
    decrease = min(rev_change)
    j = rev_change.index(decrease)
    monthly_decrease = month[j+1]


# Print the following analysis to the terminal window:
print(f'----------------------------'+'\n')
print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')
print("Total number of months: " + str(len(month)))
print("Total Revenue in period: $ " + str(total_rev))
print("Average monthly change in Revenue : $" + str(month_change))
print(f"Greatest Increase in Profits: {monthly_increase} (${increase})")
print(f"Greatest Decrease in Profits: {monthly_decrease} (${decrease})")

# Print/Export the following information into a text file:

output_path = os.path.join(r"C:\Users\eliza\Desktop\Data Analytics\Git Hub Repositories\03-Python-Challenge\PyBank\Analysis\financial_analysis.txt")
with open(output_path, 'w') as outputHeader:
    outputHeader.write(f'----------------------------')
    outputHeader.write('\n')
    outputHeader.write(f'Financial Analysis')
    outputHeader.write('\n')
    outputHeader.write(f'----------------------------')
    outputHeader.write('\n')
    outputHeader.write("Total number of months: " + str(len(month)))
    outputHeader.write('\n')
    outputHeader.write("Total Revenue in period: $ " + str(total_rev))
    outputHeader.write('\n')
    outputHeader.write("Average monthly change in Revenue : $" + str(month_change))
    outputHeader.write('\n')
    outputHeader.write(f"Greatest Increase in Profits: {monthly_increase} (${increase})")
    outputHeader.write('\n')
    outputHeader.write(f"Greatest Decrease in Profits: {monthly_decrease} (${decrease})")     
