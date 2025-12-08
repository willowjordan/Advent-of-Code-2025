# tool for solving day 2, part 2 of advent of code 2025
# author: willow jordan

import numpy as np

def main():
    # Open the file in read mode
    file = open("input.txt", "r")
    allInvalidIDs = []

    # Read character by character
    content = file.read()
    first = "" # first ID in range
    last = "" # last ID in range
    i = 0
    eof = False
    while (not eof):
        while (content[i] != '-'):
            first += content[i]
            i += 1
        i += 1
        while (content[i] != ','):
            if (content[i] == '\n'):
                eof = True
                break
            last += content[i]
            i += 1
        i += 1
        last = last.strip() # prevent newline from ending up in last iteration
        print(f"Calling getInvalidIDs with first={first} and last={last}")
        allInvalidIDs += getInvalidIDs(int(first), int(last))
        first = ""
        last = ""

    # Close the file
    file.close()

    print("Invalid IDs:")
    print(allInvalidIDs)

    # add up invalid IDs
    print(f"Sum of invalid IDs: {sum(allInvalidIDs)}")

def getInvalidIDs(rangeStart, rangeEnd):
    invalidIDs = []

    i = rangeStart
    while i <= rangeEnd:
        # get number of digits and figure out which patterns we'll need to check for
        patternOccurrancesToCheck = []
        numDigits = len(str(i))
        # patternOccurrancesToCheck are the numbers of times a string can repeat itself in an ID
        # for example, a 6 digit number could have a twice repeating or thrice repeating pattern
        for num in [2, 3, 5, 7]: # this is all we will need since the biggest ranges are 10 digits at most
            if (numDigits % num) == 0: # if number of digits is divisible by that number
                patternOccurrancesToCheck += [num]
        
        # create subrange of a single digit length to check for invalid IDs in
        subrangeStart = i # start of subrange
        subrangeEnd = (10 ** numDigits) - 1
        if subrangeEnd > rangeEnd: subrangeEnd = rangeEnd
        # use each pattern to generate the invalid IDs
        for num in patternOccurrancesToCheck:
            patternLen = numDigits // num
            pattern = str(subrangeStart)[0:patternLen] # string
            # generate invalid IDs
            while (True):
                # generate new potentially invalid ID
                newID = ''
                for i in range(0, num): # repeat num times
                    newID += pattern
                newID = int(newID)

                # increment pattern
                pattern = str(int(pattern) + 1)

                # out of bounds checking
                if (newID < subrangeStart): continue
                if (newID > subrangeEnd): break
                
                # append to return array
                invalidIDs += [newID]

        # advance to next number of digits
        i = subrangeEnd + 1
        
    # remove duplicates and return
    return list(set(invalidIDs))

if __name__ == "__main__":
    main()
    #print(getInvalidIDs(111110, 111112))