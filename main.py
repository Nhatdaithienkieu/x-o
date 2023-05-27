table = [
    ["", "", ""], 
    ["", "", ""], 
    ["", "", ""]
    ]

finished = [
    ["o", "o", "o"], 
    ["o", "x", "o"], 
    ["o", "o", "o"]
    ]

def make_move(tic_or_toe, pos_x, pos_y):
    table[pos_x][pos_y] = tic_or_toe

    print(table[0])
    print(table[1])
    print(table[2])

def check_winner():
    # check ngang x
    if finished[0][0] == "x" and finished[0][1] == "x" and finished[0][2] == "x":
        print("x wins")
    elif finished[1][0] == "x" and finished[1][1] == "x" and finished[1][2] == "x":
        print("x wins")
    elif finished[2][0] == "x" and finished[2][1] == "x" and finished[2][2] == "x":
        print("x wins")
    # check doc x
    elif finished[0][0] == "x" and finished[1][0] == "x" and finished[2][0] == "x":
        print("x wins")
    elif finished[0][1] == "x" and finished[1][1] == "x" and finished[2][1] == "x":
        print("x wins")
    elif finished[0][2] == "x" and finished[1][2] == "x" and finished[2][2] == "x":
        print("x wins")
    # check treo x
    elif finished[0][0] == "x" and finished[1][1] == "x" and finished[2][2] == "x":
        print("x wins")
    elif finished[0][2] == "x" and finished[1][1] == "x" and finished[2][0] == "x":
        print("x wins")
    # check ngang o
    elif finished[0][0] == "o" and finished[0][1] == "o" and finished[0][2] == "o":
        print("o wins")
    elif finished[1][0] == "o" and finished[1][1] == "o" and finished[1][2] == "o":
        print("o wins")
    elif finished[2][0] == "o" and finished[2][1] == "o" and finished[2][2] == "o":
        print("o wins")
    # check doc o
    elif finished[0][0] == "o" and finished[1][0] == "o" and finished[2][0] == "o":
        print("o wins")
    elif finished[0][1] == "o" and finished[1][1] == "o" and finished[2][1] == "o":
        print("o wins")
    elif finished[0][2] == "o" and finished[1][2] == "o" and finished[2][2] == "o":
        print("o wins")
    # check treo o
    elif finished[0][0] == "o" and finished[1][1] == "o" and finished[2][2] == "o":
        print("o wins")
    elif finished[0][2] == "o" and finished[1][1] == "o" and finished[2][0] == "o":
        print("o wins")
    else:
        print("it`s a draw")

#make_move("x", 1, 2)
check_winner()