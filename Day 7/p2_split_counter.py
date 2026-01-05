# tool for solving day 7, part 2 of advent of code 2025
# author: willow jordan

def main():
    # open the file in read mode
    file = open("input.txt", "r")
    # parse each line into more usable data objects
    board = []
    for line in file:
        board.append(line)

    # find starting position
    beams = [] # number of beams in each column
    for i in range(0, len(board[0])):
        if board[0][i] == 'S':
            beams.append(1)
        else:
            beams.append(0)
    
    # traverse board and adjust number of beams in each column as necessary
    for rowNum in range(2, len(board), 2):
        for colNum in range(0, len(board[rowNum])):
            if board[rowNum][colNum] == '^':
                if beams[colNum] > 0:
                    # divert beams to either side
                    beams[colNum - 1] += beams[colNum]
                    beams[colNum + 1] += beams[colNum]
                    # stop original beams
                    beams[colNum] = 0
    
    print("Number of beams: ", sum(beams))

if __name__ == "__main__":
    main()