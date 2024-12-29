import re

# Read input from file
with open("input.txt", "r") as file:
    input_text = file.read()

# Part 1
matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input_text)  # Use raw string
print("Total sum:", sum(map(lambda x: int(x[0]) * int(x[1]), matches)))


