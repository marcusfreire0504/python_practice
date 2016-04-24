# Enter the file name
filename = raw_input("Enter file name: ")
file = open(filename)

# Calculate the sum of the incomes and count the number of rows
total = 0
i = 0

for line in file:
    if not line.startswith("Income: ") : continue
    
    # Extract number from the string
    number = line[20::1]
    # Convert it to float format
    number = float (number)
    
    # Calculate the sum
    total = total + number
    
    # Count the number of rows
    i = i + 1
    
# Calculate the average
average = total/i

print "Average spam confidence:", average
 
