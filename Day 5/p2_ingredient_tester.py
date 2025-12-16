# tool for solving day 5, part 2 of advent of code 2025
# author: willow jordan

def main():
    # open the file in read mode
    file = open("input.txt", "r")
    fresh_ranges = []
    # read only the ranges, quit when we reach the halfway point
    for line in file:
        if line[0] == '\n':
            break
        fresh_ranges.append(parse_range(line.strip()))

    # sort data objects
    fresh_ranges.sort(key=lambda tup: tup[0])

    # figure out how many fresh IDs the ranges cover
    num_fresh_ids = 0
    next_id = -1 # the next ID to start the range at if necessary (this will mitigate overlapping ranges)
    for range in fresh_ranges:
        # calculate the length of the range, starting at either the first number in the range or at (end of last range) + 1, whichever is bigger
        range_start = max(range[0], next_id)
        if range_start > range[1]: continue # if entire range has been covered, skip
        num_fresh_ids += range[1] - max(range[0], next_id) + 1
        next_id = range[1] + 1
    print("Number of fresh IDs: ", num_fresh_ids)

    # close the file
    file.close()

# convert range from string to tuple of ints
def parse_range(line):
    first = ""
    last = ""
    halfway = False
    for i in range(0, len(line)):
        if line[i] == '-':
            halfway = True
        elif not halfway:
            first += line[i]
        else:
            last += line[i]
    return (int(first), int(last))

if __name__ == "__main__":
    main()