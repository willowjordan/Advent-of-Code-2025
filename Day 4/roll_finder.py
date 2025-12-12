# tool for solving day 4, part 1 of advent of code 2025
# author: willow jordan

rolls = []

def main():
    # Open the file in read mode
    file = open("input.txt", "r")

    for line in file:
        rolls.append(line.strip())

    #print(is_accessible(0, 0))
    num_accessible = 0
    for i in range(0, len(rolls)):
        for j in range(0, len(rolls[0])):
            if rolls[i][j] == '@':
                if is_accessible(i, j):
                    num_accessible += 1
    print("Number of accessible rolls:", num_accessible)

    file.close()

def is_accessible(i, j):
    # positions to check for rolls
    positions = [(i-1, j-1),
                 (i-1, j),
                 (i-1, j+1),
                 (i, j-1),
                 (i, j+1),
                 (i+1, j-1),
                 (i+1, j),
                 (i+1, j+1)]
    num_adjacent_rolls = 0
    for pos in positions:
        #print("Checking position", pos)
        # skip this position if out of bounds
        if (pos[0] < 0) | (pos[0] >= len(rolls)) | (pos[1] < 0) | (pos[1] >= len(rolls[0])): continue 
        if rolls[pos[0]][pos[1]] == '@':
            #print("Adjacent roll found")
            num_adjacent_rolls += 1
        if num_adjacent_rolls >= 4:
            return False
    return True

if __name__ == "__main__":
    main()