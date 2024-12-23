# Initialize the lists
list1 = []
list2 = []

# Open and read the file
with open("input.txt", "r") as file:
    for line in file:
        # Strip leading/trailing spaces and split the line
        line = line.strip()
        parts = line.split()
        
       # Ensure the line has exactly two values
        if len(parts) == 2 and all(part.isdigit() for part in parts):
            num1, num2 = map(int, parts)
            list1.append(num1)
            list2.append(num2)
            
# Sort the lists
list1.sort()
list2.sort()

# Calculate distance
distance = sum(abs(a - b) for a, b in zip(list1, list2))


# Print results
print("Distance:", distance)






    










