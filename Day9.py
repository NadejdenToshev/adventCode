# Part 1

with open("Solutions/input.txt", "r") as file:
    line = file.read().strip()

def make_filesystem(diskmap):
    blocks = []

    is_file = True
    id = 0
    for x in diskmap:
        x = int(x)
        if is_file:
            blocks += [id] * x
            id += 1
            is_file = False
        else:
            blocks += [None] * x
            is_file = True

    return blocks

filesystem = make_filesystem(line)

def move(arr):
    first_free = 0
    while arr[first_free] != None:
        first_free += 1

    i = len(arr) - 1
    while arr[i] == None:
        i -= 1

    while i > first_free:
        arr[first_free] = arr[i]
        arr[i] = None
        while arr[i] == None:
            i -= 1
        while arr[first_free] != None:
            first_free += 1

    return arr

def check_sum(arr):
    result = 0
    for i, x in enumerate(arr):
        if x != None:
            result += i * x
    return result

result = check_sum(move(filesystem))
print(result)

