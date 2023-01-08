import curses
import time
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLACK_AND_RED = curses.color_pair(1)
    BLUE_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)
    #    stdscr.nodelay(True)

    
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



    # ^ main menu and press Space to start (part a)
    
    # add border color to suggest game state??
    # for instance,
        # stdscr.attron(RED_AND_WHITE)
        # stdscr.border()
        # stdscr.refresh()
        # ..
        # stdscr.attroff(RED_AND_WHITE)


    plot1_win = curses.newwin(3, 3, 3, 2)
    plot2_win = curses.newwin(3, 3, 3, 9)
    plot3_win = curses.newwin(3, 3, 8, 2)
    plot4_win = curses.newwin(3, 3, 8, 9)
    instruction_win = curses.newwin(20, 3, 50, 5)
    


wrapper(main)















