import curses
from re import L
import time

FARM_COLS = 9
FARM_ROWS = 9

class Game:
    def __init__(self) -> None:
        self.farm = [
                [ ord('/') for col in range(FARM_COLS) ] for row in range(FARM_ROWS)
            ]
        self.fast_forward = False
        self.money = 0
        self.tool_bar = ['*', 'r', 'w', 'v', 'x', 'f', 'g']
        self.player_coords = [5,5] # (y, x)
        self.start_time = time.time()
        

        self.farm_pad = curses.newwin(FARM_ROWS+1, FARM_COLS+1, 1, 1)
        self.time_pad = curses.newpad(2,4)
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        sapling_color = curses.color_pair(1)
        
    def time(self) -> int:
        return time.time() - self.start_time
    def game_days(self) -> int:
        return time // 10
        
    def update(self, stdscr):
        for row in range(FARM_ROWS):
            for col in range(FARM_COLS):
                self.farm_pad.addch(row,col, self.farm[row][col], curses.color_pair(1))

        stdscr.nodelay(True)
        
        input = stdscr.getch ()
        stdscr.addch(*self.player_coords,  '@', curses.A_BLINK)
        self.farm_pad.refresh()
        print(self.player_coords)

        # arrow key movement

        if input == curses.KEY_UP:
            self.player_coords[0] -= 1
        elif input == curses.KEY_LEFT:
            self.player_coords[1] -= 1
        elif input == curses.KEY_DOWN:
            self.player_coords[0] += 1
        elif input == curses.KEY_RIGHT:
            self.player_coords[1] += 1
        
        if self.player_coords[0] < 0: self.player_coords[0] = 0
        if self.player_coords[1] < 0: self.player_coords[1] = 0
        
        return input

def main(stdscr):
    game = Game()

    while (True):
        input = game.update(stdscr)
        if input == ord('q'):
            break

curses.wrapper(main)