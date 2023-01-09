from cmath import pi
import curses
from re import L
import time
import typing
import abc
import random

FARM_COLS = 9
FARM_ROWS = 9
DAY_LENGTH = 10 # in seconds
DIMENSIONS = (30, 30)

class Sprite:
    def __init__(self, data, transform) -> None:
        self.data = data # this is pretty bad
        ((height, width), (row, col)) = transform
        self.window = curses.newwin(height, width, row, col)
    def winaddstr(self, string) -> None:
        """Purpose: calling addstr or addch to the lower right corner of a window will cause an error,
        so my workaround is to use a larger window and then resize after, which does not have the error.
        This function DOES NOT call refresh. (But does call clear, which is equivalent to erase then redrawwin"""
        len(string)
        lines = string.splitlines()
        ymax = len(lines)
        xmax = max([len(l) for l in lines])
        self.window.clear()
        self.window.resize(ymax, xmax + 1) # maybe have a conditional to only resize if it would be insufficient first
        self.window.addstr(string)
        self.window.resize(ymax, xmax)

class Crop(metaclass=abc.ABCMeta):
    """For now, all crops have 3 life stages: seed, young, and mature"""
    DAYS_PER_STAGE = 2 # in days
    def __init__(self) -> None:
        self.start_time = time.time()
    
    @abc.abstractmethod
    def appearance(self) -> str: pass
    @abc.abstractmethod
    def value(self) -> int: pass # essentialist theory of value or sth go brrr
    @abc.abstractmethod
    def days_per_stage(self) -> float: pass
    @abc.abstractmethod
    def maybe_die(self) -> bool: pass
    
    def age(self) -> float:
        return time.time() - self.start_time
    def stage(self) -> int:
        return int(self.age() // self.days_per_stage())
class Soil(Crop):
    def __init__(self) -> None:
        super().__init__()
    def appearance(self) -> str: return '_'
    def value(self) -> int: return 0
    def days_per_stage(self) -> float: return 999999.0 # I guess it doesn't really matter. maybe I should have made a "tile class" and a "crop class". not important
    def maybe_die(self): pass
class Carrot(Crop):
    def __init__(self) -> None:
        super().__init__()
    def appearance(self) -> str:
        assert(self.stage() >= 0)
        if self.stage() == 0:
            return '.'
        elif self.stage() == 1:
            return 'v'
        elif self.stage() >= 2:
            return 'V'
    def value(self) -> int:
        if self.stage() == 0:
            return 0
        if self.stage() == 1:
            return 5
        if self.stage() >= 2:
            return 10
    def days_per_stage(self) -> float:
        return 3
    def maybe_die(self) -> bool:
        return self.stage() >= 3 + random.randint(0, 4)

class Player(Sprite):
    def __init__(self, data, transform) -> None:
        super().__init__(data, transform)
    def pick_plant(self, farm: Sprite) -> Crop:
        y, x = self.window.getbegyx()
        fy, fx = farm.window.getbegyx()
        (y, x) = (y - fy, x - fx) # relative to farm
        if y in range(0, FARM_ROWS) and x in range(0, FARM_COLS):
            picked_plant = farm.data[y][x]
            farm.data[y][x] = Soil()
            return picked_plant

class Game:
    def __init__(self) -> None:
        # I think a lot of this code could be removed if it's already in update()
        farm = [
                [ Carrot() for col in range(FARM_COLS) ] for row in range(FARM_ROWS)
            ]
        farm_string =\
            str.join(
                '\n', [str.join(
                    '', [crop.appearance() for crop in line_of_crops]
                ) for line_of_crops in farm]
            )
        self.farm = Sprite(farm, ((FARM_ROWS, FARM_COLS+1), (5, 5)))
        self.farm.winaddstr(farm_string)

        self.fast_forward = False

        self.money_hud = Sprite(0, ((1, 3), (0,0))) # top left
        self.money_hud.winaddstr(f'${self.money_hud.data}')

        self.player = Player(None, ((1,2), (6, 6)))
        self.player.winaddstr('@')

        self.start_time = time.time()
        time_string = '0 days'
        self.time_hud = Sprite(0, ((1,2), (0, DIMENSIONS[1]-1-len(time_string))))
        self.time_hud.winaddstr(time_string)

        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)        
    def time(self) -> int:
        return time.time() - self.start_time
    def game_days(self) -> int:
        return int(self.time() // DAY_LENGTH)
    def update(self, stdscr):
        # refresh all windows from bottom layer to top layer. i think ideally, we would only call redrawwin when ncsry
        # also, could maybe do the thing they do in PyGame where you put them in a list and then it's neater
        stdscr.redrawwin()
        input = stdscr.getch() # this also does refresh
        self.farm.window.redrawwin()
        self.farm.window.refresh()
        self.player.window.redrawwin()
        self.player.window.refresh()
        self.money_hud.window.redrawwin()
        self.money_hud.window.refresh()
        self.time_hud.window.redrawwin()
        self.time_hud.window.refresh()

        # should probably make data used within each class, with polymorphism... seems like I'm not taking advantage of classes enough
        farm_string =\
            str.join(
                '\n', [str.join(
                    '', [crop.appearance() for crop in line_of_crops]
                ) for line_of_crops in self.farm.data]
            ) # convert 2d list into a multiline string, using join + list comprehension
        self.farm.winaddstr(farm_string)


        for y in range(FARM_ROWS):
            for x in range(FARM_COLS):
                if (self.farm.data[y][x].maybe_die()):
                    self.farm.data[y][x] = Carrot()
                    if random.choice([False, True]):
                        if y - 1 >= 0:
                            if isinstance(self.farm.data[y-1][x], Soil):
                                self.farm.data[y-1][x] = Carrot()
                    if random.choice([False, True]):
                        if y + 1 < FARM_ROWS:
                            if isinstance(self.farm.data[y+1][x], Soil):
                                self.farm.data[y+1][x] = Carrot()
                    if random.choice([False, True]):
                        if x - 1 >= 0:
                            if isinstance(self.farm.data[y][x-1], Soil):
                                self.farm.data[y][x-1] = Carrot()
                    if random.choice([False, True]):
                        if x + 1 < FARM_COLS:
                            if isinstance(self.farm.data[y][x+1], Soil):
                                self.farm.data[y][x+1] = Carrot()

        time_string = f'{self.game_days()} days'
        self.time_hud.winaddstr(time_string)
        self.time_hud.window.mvwin(0,DIMENSIONS[1]-1-len(time_string))

        money_string = f'${self.money_hud.data}'
        self.money_hud.winaddstr(money_string)

        print(self.farm.data)

        # arrow key movement
        player_y, player_x = self.player.window.getbegyx()
        if input == curses.KEY_UP:
            player_y -= 1
        elif input == curses.KEY_LEFT:
            player_x -= 1
        elif input == curses.KEY_DOWN:
            player_y += 1
        elif input == curses.KEY_RIGHT:
            player_x += 1
        if player_y < 0: player_y = 0
        if player_x < 0: player_x = 0
        maxy, maxx = stdscr.getmaxyx()
        if player_y >= maxy: player_y = maxy-1
        if player_x >= maxx: player_x = maxx-1
        self.player.window.mvwin(player_y, player_x)
        # press space to pick plant
        picked_plant = None
        if input == ord(' '):
            picked_plant = self.player.pick_plant(self.farm)
        # print(picked_plant)
        if picked_plant != None:
            self.money_hud.data += picked_plant.value()
        return input


def main(stdscr):
    game = Game()
    stdscr.nodelay(True)
    stdscr.leaveok(True)

    while (True):
        curses.napms(15) # this seems like the wrong way... but 
        input = game.update(stdscr)
        if input == ord('q'):
            break

curses.wrapper(main)