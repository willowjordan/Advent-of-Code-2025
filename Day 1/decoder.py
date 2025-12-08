# tool for solving day 1, part 1 of advent of code 2025
# author: willow jordan

# Open the file in read mode
file = open("input.txt", "r")

# Read line by line, decoding combination
currentPos = 50 # position of dial
zeroCount = 0 # number of times the dial has landed on 0
for line in file:
    amount = int(line[1:]) # how far to turn dial
    print(f"{line} - turn {amount} times")
    if line[0] == "R":
        currentPos += amount
    elif line[0] == "L":
        currentPos -= amount
    else:
        print("Warning: unrecognized direction")
    currentPos = currentPos % 100
    print(f"Current position: {currentPos}")
    if currentPos == 0:
        zeroCount += 1

print(f"The dial landed on zero exactly {zeroCount} times")

# Close the file
file.close()