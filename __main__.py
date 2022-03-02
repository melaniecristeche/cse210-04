import os
import random
from typing_extensions import Self

from game.casting.actor import Actor
from game.casting.gem import Gem
from game.casting.rock import Rock
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 25
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "Greed Game"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
PINK = Color(255,192,203)
PURPLE = Color(128,0,128)
Number_Of_Rocks = 20
Number_of_Gems = 25


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y-30)
    position = Point(x, y)
    

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    for i in range(Number_Of_Rocks):
        # text = chr(219)
        text = "@"
        #text = "()"
        x = random.randint(1, COLS - 2)
        y = random.randint(1, ROWS - 2)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        speed=Point(0,5)
    
        r = random.randint(0, 0)
        g = random.randint(1, 255)
        b = random.randint(0, 0)
        color = Color(r, g, b)
        
        rock = Rock()
        rock.set_text(text)
        rock.set_font_size(FONT_SIZE)
        rock.set_color(color)
        rock.set_position(position)
        rock.set_velocity(speed)
        cast.add_actor("rocks", rock)
        
        # next level score
        score = Director._do_updates()

        if score >= 10:
            # next level properties
            new_speed = Point(0,3)
            new_color = PURPLE
            
            rock = Rock()
            rock.set_text(text)
            rock.set_font_size(FONT_SIZE)
            rock.set_color(new_color)
            rock.set_position(position)
            rock.set_velocity(new_speed)
            cast.add_actor("rocks", rock)


        
    for i in range(Number_of_Gems):
        # text = chr(36)
        #text = "*"
        text = "*"
        x = random.randint(1, COLS - 2)
        y = random.randint(1, ROWS - 2)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        speed=Point(0,5)
    

        r = random.randint(200, 255)
        g = random.randint(200, 255)
        b = random.randint(0, 0)
        color = Color(r, g, b)
        
               
        gem = Gem()
        gem.set_text(text)
        gem.set_font_size(FONT_SIZE)
        gem.set_color(color)
        gem.set_position(position)
        gem.set_velocity(speed)
        cast.add_actor("gems", gem)

        # next level properties
        new_speed = Point(0,6)
        new_color = PINK
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()