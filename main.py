import GOL, os, time
from pytimedinput import timedInput

board = GOL.generateBoard(30,30,3)

while 1:
    time.sleep(0.3)
    txt,_ = timedInput("",timeout = 0.05)
    if txt == " ":
        board = GOL.generateBoard(100,60,3)
    os.system("clear")
    GOL.print_board(board)
    board = GOL.gameOfLife(board)