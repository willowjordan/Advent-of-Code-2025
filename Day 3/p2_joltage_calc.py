# tool for solving day 3, part 1 of advent of code 2025
# author: willow jordan

JOLTAGE_DIGITS = 12 # number of batteries that can be flipped on per bank

def main():
    # Open the file in read mode
    file = open("input.txt", "r")
    
    # Read line by line
    joltageSum = 0
    for line in file:
        joltageSum += getRowMaxJoltage(line.strip())
    print(f"Joltage Sum: {joltageSum}")

def getRowMaxJoltage(bank):
    maxJoltage = ""
    startPos = 0
    for i in range(0, JOLTAGE_DIGITS): # repeat 12 times
        tempMax = 0
        tempMaxPos = -1
        for j in range(startPos, len(bank) - (JOLTAGE_DIGITS - i) + 1):
            currDigit = int(bank[j])
            if (currDigit > tempMax):
                tempMax = currDigit
                tempMaxPos = j
        # append maximum to string
        maxJoltage += str(tempMax)
        startPos = tempMaxPos + 1
    
    #print(f"Max joltage for row: {maxJoltage}")
    return int(maxJoltage)

if __name__ == "__main__":
    main()
    #getRowMaxJoltage("234234234234278")