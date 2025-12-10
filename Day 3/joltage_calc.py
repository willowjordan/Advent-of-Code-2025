# tool for solving day 3, part 1 of advent of code 2025
# author: willow jordan

def main():
    # Open the file in read mode
    file = open("input.txt", "r")
    
    # Read line by line
    joltageSum = 0
    for line in file:
        joltageSum += getRowMaxJoltage(line.strip())
    print(f"Joltage Sum: {joltageSum}")

def getRowMaxJoltage(bank):
    maxFirstDigit = 0
    maxSecondDigit = 0
    for i in range(0, len(bank)):
        currDigit = int(bank[i])
        if (currDigit > maxFirstDigit) & (i < (len(bank)-1)): # if current digit is the highest we've found and is NOT the last digit
            maxFirstDigit = currDigit
            maxSecondDigit = 0
        elif (currDigit > maxSecondDigit): # if current digit is the highest we've found that occurs after the ACTUAL highest digit
            maxSecondDigit = currDigit
    return (maxFirstDigit * 10 + maxSecondDigit)

if __name__ == "__main__":
    main()