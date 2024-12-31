import re
from functools import reduce

# Part 1

# Read input from file
with open("input.txt", "r") as file:
    input_text = file.read()

# Extracts all "mul(a,b)" from the input text, 
# multiplies the two numbers (a and b) in each match, and computes their total sum
matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input_text)
print("Total sum:", sum(map(lambda x: int(x[0]) * int(x[1]), matches)))



# Part2
""" This function processes substrings from input text, 'do', 'don't', and 'mu(a,b)'.
    It calculate a sum by multiplaying numbers in 'mul(a,b)', but only if process is enabled.
    'do' enables processing, 'don't' disables it, and the result is printed at the end.
"""
def process(carry, match):
    if carry['enabled'] and match[0].startswith('mul('): 
        return {'sum': carry['sum'] + int(match[1]) * int(match[2]), 'enabled': True}
    elif match[0].startswith('don'):
        return {'sum': carry['sum'], 'enabled': False}
    elif match[0].startswith('do'):
        return {'sum': carry['sum'], 'enabled': True}
    else:
        return carry

matches = re.findall('(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))', input_text)
result = reduce(process, matches, {'sum': 0, 'enabled': True})
print("Total sum:", result['sum'])

