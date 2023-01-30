import argparse
import os
import time

from pytimedinput import timedInput

import GOL


def parseVars():
    descStr = "Game of life"
    parser = argparse.ArgumentParser(description=descStr)
    parser.add_argument('--height', dest = 'height', required = True)
    parser.add_argument('--width', dest = 'width', required = True)
    parser.add_argument('--odds', dest = 'odds', required = False)
    parser.add_argument("--time", dest = "time", required = False)

    args = parser.parse_args()

    height = args.height
    width  = args.width
    odds   = 3
    time   = 0.2

    if args.odds:
        odds = args.odds
    if args.time:
        time = args.time

    return [int(height), int(width), int(odds), float(time)]


settings = parseVars()

board = GOL.generateBoard(settings[1], settings[0], settings[2])




while 1:
    time.sleep(settings[3])
    txt,_ = timedInput("",timeout = 0.05)
    if txt == " ":
        board = GOL.generateBoard(settings[1], settings[0], settings[2])
    os.system("clear")
    GOL.print_board(board)
    board = GOL.gameOfLife(board)
