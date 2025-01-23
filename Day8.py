# Part 1

with open("Solutions/input.txt", "r") as file:
    grid = file.read().strip().split("\n")

n = len(grid)

def locate_antennas(grid):
    """Locates antennas and stores them by frequency."""
    antenna_dict = {}
    rows = len(grid)
    cols = len(grid[0]) #Assuming the grid is square

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.':
              frequency = grid[r][c]
              antenna_dict.setdefault(frequency, []) # if not found, create an empty list
              antenna_dict[frequency].append((r, c))

    return antenna_dict


def calculate_antinodes(antenna_dict, n):
    """Calculates antinode locations based on antenna positions."""
    antinode_set = set()

    def in_bounds(r, c):
        return 0 <= r < n and 0 <= c < n


    for freq, antenna_coords in antenna_dict.items():
        for i in range(len(antenna_coords)):
            for j in range(i + 1, len(antenna_coords)):
                r1, c1 = antenna_coords[i]
                r2, c2 = antenna_coords[j]

                dr = r2 - r1
                dc = c2 - c1

                r_ant1 = r1 - dr
                c_ant1 = c1 - dc
                r_ant2 = r2 + dr
                c_ant2 = c2 + dc

                if in_bounds(r_ant1, c_ant1):
                  antinode_set.add((r_ant1, c_ant1))
                if in_bounds(r_ant2, c_ant2):
                  antinode_set.add((r_ant2, c_ant2))

    return antinode_set

def count_antinodes(antinode_set):
    """Counts the number of unique antinode locations."""
    count = len(antinode_set)
    return count

def output_result(antinode_count):
    """Prints the final antinode count."""
    print(antinode_count)

antenna_locations = locate_antennas(grid)
antinode_locations = calculate_antinodes(antenna_locations, n)
antinode_count = count_antinodes(antinode_locations)
output_result(antinode_count)

        


