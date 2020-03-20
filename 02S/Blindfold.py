import sys
input = sys.stdin.readline

h = int(input())
w = int(input())

grid = [[j for j in input()[:-1]] for i in range(h)]
# print(grid)

num_of_moves = int(input())
moves = [input()[:-1] for i in range(num_of_moves)]
moves = moves[::-1] # Treat R like L
# print(moves)

def valid(index, jindex):
    if not 0 <= index < h or not 0 <= jindex < w or grid[index][jindex] == "X":
        return False
    return True

def translate(pos):
    if pos[2] < 0:
        pos[2] += 4
    pos[2] %= 4
    direction = pos[2]

    if pos[2] == 0:
        pos[0] -= 1
    elif pos[2] == 1:
        pos[1] -= 1
    elif pos[2] == 2:
        pos[0] += 1
    elif pos[2] == 3:
        pos[1] += 1

def reachable(index, jindex):
#     print(index, jindex, end = "")

    position = [index, jindex, 0]
    all_valid = True
    for i in moves: # Up
        if i == "F":
            translate(position)
        elif i == "L":
            position[2] -= 1
        else:
            position[2] += 1

        if not valid(position[0], position[1]):
            all_valid = False
            break
    
    if all_valid:
        return True
    
    position = [index, jindex, 1]
    all_valid = True
    for i in moves: # Right
        if i == "F":
            translate(position)
        elif i == "L":
            position[2] -= 1
        else:
            position[2] += 1

        if not valid(position[0], position[1]):
            all_valid = False
            break


    if all_valid:
        return True
    
    position = [index, jindex, 2]
    all_valid = True
    for i in moves: # Down
        if i == "F":
            translate(position)
        elif i == "L":
            position[2] -= 1
        else:
            position[2] += 1

        if not valid(position[0], position[1]):
            all_valid = False
            break


    if all_valid:
        return True
    
    position = [index, jindex, 3]
    all_valid = True
    for i in moves: # Left
        if i == "F":
            translate(position)
        elif i == "L":
            position[2] -= 1
        else:
            position[2] += 1

        if not valid(position[0], position[1]):
            all_valid = False
            break


    if all_valid:
        return True

    return False

for index, i in enumerate(grid):
    for jindex, j in enumerate(i):
        if j == ".":
            if reachable(index, jindex):
                print("*", end = "")
            else:
                print(".", end = "")
        else:
            print("X", end = "")

    print("")
