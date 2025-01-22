# Part 1

from itertools import product

with open("Solutions/input.txt", "r") as file:
    lines = file.read().strip().split("\n")

result = 0
for i, line in enumerate(lines):
    parts = line.split()
    value = int(parts[0][:-1])
    nums = list(map(int, parts[1:]))

    def test(combination):
        result = nums[0]
        for i in range(1, len(nums)):
            if combination[i-1] == "+":
                result += nums[i]
            else:
                result *= nums[i]
        return result

    for combination in product("*+", repeat=len(nums)-1):
        if test(combination) == value:
            result += value
            break

print(result)


# Part 2

from itertools import product

with open("Solutions/input.txt", "r") as file:
    lines = file.read().strip().split("\n")

ans = 0
for i, line in enumerate(lines):
    parts = line.split()
    value = int(parts[0][:-1])
    nums = list(map(int, parts[1:]))

    def test(combo):
        ans = nums[0]
        for i in range(1, len(nums)):
            if combo[i-1] == "+":
                ans += nums[i]
            elif combo[i-1] == "|":
                ans = int(f"{ans}{nums[i]}")
            else:
                ans *= nums[i]
        return ans

    for combo in product("*+|", repeat=len(nums)-1):
        if test(combo) == value:
            ans += value
            break

print(ans)