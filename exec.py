import itertools
from collections import namedtuple
import go_mutable_joe as util

N = 19
NN = N * N
WHITE, BLACK, EMPTY = 'O', 'X', '.'

def draw_board(board):
    Point = namedtuple('Point', 'x y')

    # Add row of letters for place naming
    print("\t", end = "  ")
    for kk in range(N):
        print(chr(kk + 97), end = " ")
    print("")

    for ii in range(N):
        # Add column of numbers for place naming
        print("\t" + str(ii + 1), end = " ")
        
        for jj in range(N):
            oneDC = N*ii + jj
            if board[oneDC] == WHITE:
                print(WHITE, end = " ")
            elif board[oneDC] == BLACK:
                print(BLACK, end = " ")
            else:
                print ("+", end = " ")
        print(" \n", end = " ")


def main():
    print("\nSTART GAME! \n")
    board = NN*EMPTY
    draw_board(board)
    print("Black turn: ")
    pInput = "abcdefg"
    turns = 0
    while pInput != "end":
        pInput = input()
        if("end" in pInput):
            pInput = "end"
            break

        lett, num = pInput.split(", ")
        turns += 1
        pointIn = (int(num) - 1)*N + ord(lett) - 97

        if(not turns%2):
            color = BLACK
        else:
            color = WHITE          

        board = util.place_stone(color, board, pointIn) # go_mutable place_stone
        draw_board(board)


        if(turns > 1000):
            pInput = "end"


if __name__ == "__main__":
    main()