# tool for solving day 6, part 1 of advent of code 2025
# author: willow jordan

def main():
    # open the file in read mode
    file = open("input.txt", "r")

    # parse each line into more usable data objects
    operators = []
    numbers = []
    # read first line
    currNum = ''
    for ch in file.readline():
        if (ch == ' ') | (ch == '\n'): 
            if currNum != '':
                numbers.append([int(currNum)])
                currNum = ''
        else:
            currNum += ch  
    # read all other lines
    currNum = ''
    for line in file:
        i = 0 # problem number
        for ch in line:
            if (ch == ' ') | (ch == '\n'): 
                if currNum != '':
                    numbers[i].append(int(currNum))
                    currNum = ''
                    i += 1
            elif (ch == '+') | (ch == '*'):
                operators.append(ch)
            else:
                currNum += ch
    
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