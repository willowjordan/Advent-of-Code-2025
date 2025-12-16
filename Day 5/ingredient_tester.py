# tool for solving day 5, part 1 of advent of code 2025
# author: willow jordan

def main():
    # open the file in read mode
    file = open("input.txt", "r")
    fresh_ranges = []
    ingredients = []
    halfway = False # true if we've reached the halfway point of file
    # parse each line into more usable data objects
    for line in file:
        if line[0] == '\n':
            halfway = True
        elif not halfway:
            fresh_ranges.append(parse_range(line.strip()))
        else:
            ingredients.append(int(line.strip()))

    # sort data objects
    fresh_ranges.sort(key=lambda tup: tup[0])
    ingredients.sort()

    # get the number of fresh ingredients
    num_fresh_ingredients = 0
    #fresh_ingredient_list = [] # debug
    j = 0 # position in ingredients array
    for curr_range in fresh_ranges:
        if j >= len(ingredients): break # out of ingredients
        while j < len(ingredients):
            if ingredients[j] > curr_range[1]: break # go to next fresh range
            if ingredients[j] >= curr_range[0]: # ingredient in range, add to total
                num_fresh_ingredients += 1
                #fresh_ingredient_list.append(ingredients[j])
            j += 1 # go to next ingredient
    print("Number of fresh ingredients: ", num_fresh_ingredients)
    #print("Fresh ingredient list: ", fresh_ingredient_list)

    # close the file
    file.close()

# convert range from string to tuple of ints
def parse_range(line):
    first = ""
    last = ""
    halfway = False
    for i in range(0, len(line)):
        if line[i] == '-':
            halfway = True
        elif not halfway:
            first += line[i]
        else:
            last += line[i]
    return (int(first), int(last))

if __name__ == "__main__":
    main()