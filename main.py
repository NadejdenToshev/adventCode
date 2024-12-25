# Read reports from the input file
reports = []
with open("input.txt", "r") as file:
    for line in file:
        reports.append(list(map(int, line.split())))

# Function to detrmine the number of safe reports
def count_safe_reports(reports):
    num_safe = 0 # Counter for safe reports
    for r in reports:
        # Check if the report is either all increasing or all decreasing
        is_increasing = all(1 <= y - x <= 3 for x,y in zip(r, r[1:]))
        is_decreasing = all(1 <= x - y <= 3 for x,y in zip(r, r[1:]))

        # A report is safe if it is either entirely increasing or entirely decreasing
        if is_increasing or is_decreasing:
            num_safe += 1 # Increment the safe report counter
    return num_safe

# Count and print the number of safe reports
num_safe_reports = count_safe_reports(reports)
print("Number of safe reports:", num_safe_reports)






    