# tool for solving day 6, part 2 of advent of code 2025
# author: willow jordan

def main():
    # open the file in read mode
    file = open("input.txt", "r")

    # parse lines into list of strings (basically 2d array)
    lines = []
    for line in file:
        lines.append(line)
    # get number of digits in each number and starting multiplier for adding numbers to array
    #NUM_DIGITS = len(lines) - 1
    #multiplier = pow(10, (NUM_DIGITS-1))

    operators = []
    numbers = []
    # parse file column by column
    currProblemNums = []
    for j in range(0, len(lines[0])):
        currNum = ""
        for i in range(0, len(lines)):
            if (lines[i][j] == '\n'): break
            if (lines[i][j] == ' '): continue
            if (lines[i][j] == '+') | (lines[i][j] == '*'):
                operators.append(lines[i][j])
            else:
                currNum += lines[i][j]
        if currNum != "": # if a number was found
            currProblemNums.append(int(currNum))
            currNum = ""
        else: # line was all spaces, end of problem
            numbers.append(currProblemNums)
            currProblemNums = []
    
    # solve problems
    total = 0
    for i in range(0, len(operators)):
        # start at 0 for addition, 1 for multiplication
        prob_solution = 0
        if operators[i] == '*': prob_solution = 1
        for num in numbers[i]:
            if operators[i] == '+':
                prob_solution += num
            else:
                prob_solution *= num
        total += prob_solution
    print("Sum of all problem answers: ", total)
        
    # close the file
    file.close()

if __name__ == "__main__":
    main()