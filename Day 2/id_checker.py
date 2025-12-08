# tool for solving day 2, part 1 of advent of code 2025
# author: willow jordan

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
        numDigits = len(str(i))
        
        if (numDigits % 2 == 0): # skip odd numbers of digits
            # create subrange of a single digit length to check for invalid IDs in
            subrangeStart = i # start of subrange
            subrangeEnd = (10 ** numDigits) - 1
            if subrangeEnd > rangeEnd: subrangeEnd = rangeEnd
            patternLen = numDigits // 2
            pattern = str(subrangeStart)[0:patternLen] # string
            # generate invalid IDs
            while (True):
                # generate new potentially invalid ID
                newID = int(pattern + pattern)

                # increment pattern
                pattern = str(int(pattern) + 1)

                # out of bounds checking
                if (newID < subrangeStart): continue
                if (newID > subrangeEnd): break
                
                # append to return array
                invalidIDs += [newID]

        # advance to next number of digits
        i = (10 ** numDigits)
        
    return invalidIDs

if __name__ == "__main__":
    main()