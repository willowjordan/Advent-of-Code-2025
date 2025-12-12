# tool for solving day 4, part 2 of advent of code 2025
# author: willow jordan

def main():
    # Open the file in read mode
    file = open("input.txt", "r")

    rolls = []
    for line in file:
        rolls.append(line.strip())

    num_accessible = 0
    
    while(True):
        new_num_accessible = remove_accessible(rolls)
        num_accessible += new_num_accessible
        if new_num_accessible == 0: break

    print("Number of accessible rolls:", num_accessible)

    file.close()

# scan rolls list (list of strings) for accessible rolls and remove them (replace with periods)
# return the number of accessible rolls found in this iteration
def remove_accessible(rolls):
    num_accessible = 0
    for i in range(0, len(rolls)):
        for j in range(0, len(rolls[0])):
            if rolls[i][j] == '@':
                if is_accessible(rolls, i, j):
                    rolls[i] = rolls[i][0:j] + '.' + rolls[i][j+1:len(rolls[i])] # remove the roll by replacing with a period
                    num_accessible += 1
    return num_accessible

def is_accessible(rolls, i, j):
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
        # skip this position if out of bounds
        if (pos[0] < 0) | (pos[0] >= len(rolls)) | (pos[1] < 0) | (pos[1] >= len(rolls[0])): continue 
        if rolls[pos[0]][pos[1]] == '@':
            num_adjacent_rolls += 1
        if num_adjacent_rolls >= 4:
            return False
    return True

if __name__ == "__main__":
    main()