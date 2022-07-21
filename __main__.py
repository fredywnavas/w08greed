from gc import collect
import os
import random

from game.casting.actor import Actor
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
from game.casting.falling_artifact import FallingArtifact
from game.casting.power_ups import PowerUp

FRAME_RATE = 30 # was 12
MAX_X = 900
MAX_Y = 600
FLOOR = 580
CELL_SIZE = 20
FONT_SIZE = 20
#below is a testing section
banner_size = 107

COLS = 60
ROWS = 40
CAPTION = "Greed"

WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 55 # was 40

gems = 0
rocks = 0
pu = 0
cur = 0
rando = 0
checks = 0

def main():
    
    power_up = PowerUp()
    
    # create the cast
    cast = Cast()
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service, cast, power_up)
    
    # create the banner this is the score board
    banner = Actor()
    banner.set_text("")
    
    #below is the original code and below that is the test code
    banner.set_font_size(FONT_SIZE)
    #banner.set_font_size(banner_size) #test code
    
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_game_object("banners", banner)
    
    # create the player the objecty that moves around.
    x = int(MAX_X / 2)
    y = FLOOR
    #print('this is the floor', FLOOR, 'this is the x', x, 'this is the y' , y) # debugging
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    
    #original code below
    player.set_font_size(FONT_SIZE)
    #player.set_font_size(banner_size)
    
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_game_object("players", player)
      
    if director._points < 100:

        for obj in range(DEFAULT_ARTIFACTS): #in range of the total number of falling items
            global checks
            checks += 1
            n = obj % 5
            if(n == 0):
                text = "*" #this is the gem
                global gems 
                gems += 1
                #global checks
                #checks += 1
                
            elif(n == 1): #if (n !=0):  #this is the original
                text = "O" #this is the rock
                global rocks
                rocks += 1
                #checks += 1
                
            elif(n == 2):
                text = 'm'
                global pu
                pu += 1
                #global checks
                #checks += 1
                
            elif(n == 3 ):
                text = 'c'
                global cur
                cur += 1
            
            else:
                text = 'r'
                global rando
                rando += 1
                
            print(f"this is {text}")
            x = random.randint(1, MAX_X)
            # y = FONT_SIZE
            y = random.randint(1, MAX_Y)
            position = Point(x, y)
            #position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            point = Point
            
            #falling artifacts that player will collect and avoid
            falling_artifact = FallingArtifact()
            falling_artifact.set_text(text)
            falling_artifact.set_font_size(FONT_SIZE)
            falling_artifact.set_color(color)
            falling_artifact.set_position(position)
            
            if (text == "O"):
                falling_artifact.set_points(-1)
            
            if (text =="*"):
                falling_artifact.set_points(2)
                
            if (text == "m"):
                base = 1 
                falling_artifact.set_points(base)
                print('you got a bonus')
                
            if text == 'c':
                negamult = 0
                falling_artifact.set_points(negamult)
                
            if text == 'r':
                falling_artifact.set_points(1)
                
                

            cast.add_game_object("falling_artifacts", falling_artifact)

    # start the game
    director.start_game()
    #print statements below are for debuggin 
    print('the total number of checks',checks)
    print('the starting total number for gems is',gems)
    print('the starting total number for rocks is',rocks)
    print('the starting total number of powerup', pu)
    print('the starting total number 0f curses', cur)
    print('the starting total number of randomizer items is ', rando)
    print('the starting total number of falling artifacts', DEFAULT_ARTIFACTS)
    print(f'the score ended at  {director._points: .0f}')
    
if __name__ == "__main__":
    main()