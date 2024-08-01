from curses import wrapper
import random

BOARD_WIDTH = (7*3+8+2)
BOARD_X_OFFSET = (80-BOARD_WIDTH)//2
BOARD_Y_OFFSET = 10

def print_background(stdscr):
    """prints the board background"""
    stdscr.addstr(9, BOARD_X_OFFSET, "V" * BOARD_WIDTH )
    stdscr.addstr(17, BOARD_X_OFFSET, "^" * BOARD_WIDTH )
    for i in range(7):
        stdscr.addstr(10+i, BOARD_X_OFFSET, "|")
        stdscr.addstr(10+i, BOARD_X_OFFSET+BOARD_WIDTH-1, "|")



def print_board(stdscr, board):
    """Prints the board to the screen. The board is printed in the center of an 80*24 terminal"""
    """24-9""" 
    for i in range(7):
        stdscr.addstr(10+i, BOARD_X_OFFSET, "| " + "".join(["("+str(j)+") " for j in board[i]]) +"|")
    stdscr.refresh()
    stdscr.getch()

def main(stdscr):
    stdscr.clear()
    print_background(stdscr)
    board = [[random.randint(1, 9) for i in range(7)] for j in range(7)]
    print_board(stdscr, board)
    stdscr.getch()


if __name__ == '__main__':
    wrapper(main)
