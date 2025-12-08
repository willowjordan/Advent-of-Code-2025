# tool for solving day 1, part 2 of advent of code 2025
# author: willow jordan

# Open the file in read mode
file = open("input.txt", "r")

# Read line by line, decoding combination
currentPos = 50 # position of dial
zeroCount = 0 # number of times the dial has CROSSED 0
for line in file:
    amount = int(line[1:]) # how far to turn dial
    origPos = currentPos
    if line[0] == "R":
        currentPos += amount
    elif line[0] == "L":
        currentPos -= amount
    else:
        print("Warning: unrecognized direction")
    #print(f"\nStarting position: {origPos}")
    #print(line)
    #print(f"Before reduction, position is {currentPos} and zero count is {zeroCount}")

    # update zero count
    if (currentPos > 99): # if count is too high
        zeroCount += currentPos // 100
    elif (currentPos <= 0): # if count is too low or is 0
        # first bring position up to (-99 to 0) range, then check if dial actually crossed 0 or if it started there
        zeroCount += abs(currentPos) // 100
        # if dial was brought from a positive position to a negative or zero position, increase count
        if (origPos > 0):
            zeroCount += 1
    # update position
    currentPos %= 100

    #print(f"After reduction, position is {currentPos} and zero count is {zeroCount}")

print(f"The dial landed on zero exactly {zeroCount} times")

# Close the file
file.close()