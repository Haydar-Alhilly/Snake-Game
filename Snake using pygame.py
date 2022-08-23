# first you should install py game library

import pygame as pg
from pygame import locals
import random
import time
pg.font.init()

# setting up the window
WIDTH, HEIGHT = 600, 400
border = pg.Rect(10, 10, 580, 480)
border2 = pg.Rect(15, 15, 570, 470)
cell_window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("SNAKE GAME!")
clock = pg.time.Clock()

# SOME COLORS(IN RGB VALUES) WE USE 
BLACK = (0, 0, 0)
GREY = (204, 200, 188)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (235, 100 , 52)

# THIS IS TO SET UP THE FRAMES SETTING
FPS = 10

# the snake and food size
SIZEXY = 25

# the starting direction of the snake
DIRECTION = 'right'

# here i put the font desired as a variable
msg_font_style = pg.font.SysFont('ubuntu', 30)
score_font_style = pg.font.SysFont('ubuntu', 25)

# the starting postion of the snake head
snake_POSX = WIDTH / 2 
snake_POSY = HEIGHT / 2

#this is the first postion of food
foodX = round(random.randint(0, WIDTH - SIZEXY)/25)*25  
foodY = round(random.randint(0, HEIGHT - SIZEXY)/25)*25 # these are (x,y) food position

# the starting value of score
score = 0 

# this is the snake body values as a list and the length
SNAKE_PARTS = []
lengthOf_snake = 1

#the while loop conditions
#game_close = False
#game_over = False


#THIS FUNCTION FOR SHOWING THE GAME OVER MESSAGE
def end_message():
    letter = msg_font_style.render("you've Lost.", True, RED)
    cell_window.blit(letter, (230 , 170))


#THIS FUNCTION FOR PRINTING OUT THE SCORE
def show_score(score):
    score_value = score_font_style.render("Score: " + str(score), True, YELLOW)
    cell_window.blit(score_value, [0, 0])


#this function for drawing the snake body
def the_snake(SNAKE_PARTS, SIZEXY):
    for part in SNAKE_PARTS:
        #Fucking_snake = pg.Rect(part[0] , part[1], SIZEXY, SIZEXY)
        pg.draw.rect(cell_window, RED, [part[0], part[1], SIZEXY, SIZEXY])


# the direction of the snake
def snake_direction(keys_pressed):
    global DIRECTION
    if keys_pressed[pg.K_UP]:
        DIRECTION = 'up'
    if keys_pressed[pg.K_DOWN]:
        DIRECTION = 'down'
    if keys_pressed[pg.K_LEFT]:
        DIRECTION = 'left'
    if keys_pressed[pg.K_RIGHT]:
        DIRECTION = 'right'


#this function to move the snake depinding on the direction
def snake_move():
    global DIRECTION, snake_POSX, snake_POSY
    pace = 25
    if DIRECTION == 'right': #and snake_POSX + pace < R_border:
        snake_POSX = (snake_POSX + pace) % WIDTH
    if DIRECTION == 'left': #and snake_POSX - pace > L_border:
        snake_POSX = (snake_POSX - pace) % WIDTH
    if DIRECTION == 'up': #and snake_POSY - pace > U_border:
        snake_POSY = (snake_POSY - pace) % HEIGHT
    if DIRECTION == 'down': #and snake_POSY + pace < D_border:
        snake_POSY = (snake_POSY + pace) % HEIGHT


#for growing the snake and del the tail if needed
def snake_growing():
    SNAKE_PARTS.append([snake_POSX, snake_POSY])
    if len(SNAKE_PARTS) > lengthOf_snake:
        del SNAKE_PARTS[0]


#function for the snake when eating the food
def eating():
    global lengthOf_snake, score, foodX, foodY
    if snake_POSX == foodX and snake_POSY == foodY:
        foodX = round(random.randint(0, WIDTH - SIZEXY)/25)*25  
        foodY = round(random.randint(0, HEIGHT - SIZEXY)/25)*25 # these are (x,y) food position
        lengthOf_snake += 1
        score += 500

# if the snake ate itself
def losing():
    global SNAKE_PARTS
    if SNAKE_PARTS[0] in SNAKE_PARTS[1:]:
        cell_window.fill(BLACK)
        end_message()
        pg.display.flip()
        #time.sleep(3)
        game_close = True
        #print("your best score is " + str(score))
        
        

# THIS FUNCTION IS specified FOR OUR DRAWING  in GAME like a snake and food and the colors
def draw_content(SNAKE_PARTS,SIZEXY, score):
    cell_window.fill(BLACK)
    pg.draw.rect(cell_window, ORANGE, [foodX, foodY, SIZEXY, SIZEXY])
    the_snake(SNAKE_PARTS, SIZEXY)
    show_score(score)
    pg.display.update()


# the main function that holds the main logic and rule of the game
def run_game():
    #global game_over
    #global game_close
    game_close = False
    game_over = False
    while not game_over:
        
        while game_close is True:
            cell_window.fill(BLACK)
            end_message()
            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_HOME:
                        run_game()
                    if event.key == pg.K_END:
                        game_over = True
                        game_close = False
                        print("your best score is " + str(score))

        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game_over = True
        keys_pressed = pg.key.get_pressed()
        snake_direction(keys_pressed)
        snake_move()
        # here we put the hiting border losing function if wanted
        draw_content(SNAKE_PARTS, SIZEXY, score) 
        snake_growing()
        losing()
        eating()
    pg.quit()
    quit()


if __name__ == "__main__":
    run_game()
