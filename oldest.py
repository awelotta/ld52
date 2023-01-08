import curses
import time
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    BLACK_AND_RED = curses.color_pair(1)
    BLUE_AND_BLACK = curses.color_pair(2)
#    stdscr.nodelay(True)

    plot1_win = curses.newwin(3, 1, 3 ,3)
    plot2_win = curses.newwin(7, 1, 3 ,3)
    plot3_win = curses.newwin(3, 7, 3 ,3)
    plot4_win = curses.newwin(7, 7, 3 ,3)

    stdscr.clear()
    stdscr.addstr(2, 15, "HIT SPACE TO PLAY")
    stdscr.addstr(4, 15, "YOU'VE COLLECTED [THESE PLANTS]", curses.A_BOLD)
    stdscr.addstr(6, 15, "YOU'VE MADE [foods]", curses.A_BOLD)

    while True:
        key = stdscr.getkey()
        if key == " ":
            break
        elif key == None:
            pass
    stdscr.addstr(8, 15, "READY", BLACK_AND_RED)
    stdscr.refresh()
    time.sleep(1.9)
    stdscr.border()

wrapper(main)





