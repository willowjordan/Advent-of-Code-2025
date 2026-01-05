# tool for solving day 7, part 1 of advent of code 2025
# author: willow jordan

def main():
    # open the file in read mode
    file = open("input.txt", "r")
    # parse each line into more usable data objects
    board = []
    for line in file:
        board.append(line)

    # scan first row
    beamLocations = []
    splitCount = 0
    for i in range(0, len(board[0])):
        if board[0][i] == 'S':
            beamLocations.append(i)
            break
    # scan remaining rows
    for i in range(1, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == '^':
                if j in beamLocations:
                    splitCount += 1
                    beamLocations.remove(j)
                    if (j-1) not in beamLocations:
                        beamLocations.append(j-1)
                    if (j+1) not in beamLocations:
                        beamLocations.append(j+1)

    print("Split count: ", splitCount)
    # close the file
    file.close()

if __name__ == "__main__":
    main()