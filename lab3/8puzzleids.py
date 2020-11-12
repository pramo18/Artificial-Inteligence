import copy, math
# Depth first search in search of target - Using Recursion

target = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 0]]

def solve(src, target, limit, visited_states):
    if src == target:
        print("Target is Reached in Stage : ", limit)
        return True
    if limit >= 12:
        return False
    visited_states.append(src)
    actions = possible_moves(src, visited_states)
    new_move = []
    min = math.inf
    for action in actions:
        if action not in visited_states and manhattan(action, target, limit) < min:
            min = manhattan(action, target, limit)
            new_move = action
    print("Stage : ", limit+1)
    display(new_move)
    if solve(new_move, target, limit+1, visited_states) is True:
        return True
    return False
    # Base case if Target found
    # Base case if limit exceeded
    # Add source to visited_states
    # Find possible slides up, down, left right to current empty site
    ### Jump to possible_moves function
    # For all possible moves got from the possible moves function
    # Check if src equals to new targets
    # Return True if target found in given depth limit


def index(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


def possible_moves(state, visited_states):
    # Find index of empty spot and assign it to b
    b = index(state, 0)
    #'d' for down, 'u' for up, 'r' for right, 'l' for left - directions array
    #Add all possible direction into directions array - Hint using if statements
    # If direction is possible then add state to move
    d = []
    if b[0] < 2:
        d.append('d')
    if b[0] > 0:
        d.append('u')
    if b[1] < 2:
        d.append('r')
    if b[1] > 0:
        d.append('l')
    # for all possible directions find the state if that move is played
    ### Jump to gen function to generate all possible moves in the given directions
    pos_moves = []
    for i in d:
        move = gen(state, i, b)
        if move not in visited_states:
            pos_moves.append(move)
    # return all possible moves only if the move not in visited_states
    return pos_moves


def gen(state, m, b): # m(move) is direction to slide, b(blank)is index of empty spot
    # create a copy of current state to test the move
    temp = copy.deepcopy(state)
    if m == 'u':
        temp[b[0]][b[1]] = temp[b[0] - 1][b[1]]
        temp[b[0] - 1][b[1]] = 0
    elif m == 'd':
        temp[b[0]][b[1]] = temp[b[0] + 1][b[1]]
        temp[b[0] + 1][b[1]] = 0
    elif m == 'l':
        temp[b[0]][b[1]] = temp[b[0]][b[1] - 1]
        temp[b[0]][b[1] - 1] = 0
    elif m == 'r':
        temp[b[0]][b[1]] = temp[b[0]][b[1] + 1]
        temp[b[0]][b[1] + 1] = 0
    # if move is to slide empty spot to the left and so on
    # return new state with tested move to later check if "src == target"
    return temp


def manhattan(src, target, depth):
    sum = 0
    for i in range(3):
        for j in range(3):
            if src[i][j] != 0:
                b = index(src, src[i][j])
                c = index(target, src[i][j])
                sum += (abs(b[0]-c[0])+(abs(b[1]-c[1])))
    # Return Min depth at which the target was found
    return sum

def display(table):
    for r in table:
        for c in r:
            if c == None:
                print(" ", end=" | ")
            else:
                print(c, end=" | ")
        print()
    print()


src = []
print("Enter the Source state : ")
for _ in range(3):
    row = input().split()
    src.append(row)
for i in range(3):
    for j in range(3):
        src[i][j] = int(src[i][j])
if solve(src, target, 0, []) is True:
    print("Success :)")
else:
    print("It's IMPOSSIBLE reaching the TARGET from the provided SOURCE state..!  :(")
