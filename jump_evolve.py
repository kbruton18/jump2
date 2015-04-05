# jump evolved!

import pygame, sys
import math
import random
from pygame.locals import *

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PRETTY_BLUE = (135,206,250)


pygame.init()
#show game name
pygame.display.set_caption('JUMP GAME')
clock = pygame.time.Clock()
#set up display
display = pygame.display.set_mode((800, 500))
screen = pygame.display.get_surface()
screen.convert()


def game_function (ann, display=False):

    # starting position of circle
    player_x = 100
    player_y = 440
    player_reached_top = False

    # change in velocity
    player_vy = 0
    # change in acceleration
    player_ay = 1

    # obstacle 1
    obstacle_one_x = 800
    obstacle_one_y = 440
    obstacle_one_vx = 8

     # obstacle 2
    obstacle_two_x = obstacle_one_x + 400
    obstacle_two_y = 440
    obstacle_two_vx = 8

     # jump boolean
    cycle_finished = True
    jump_cycle = False
    reached_top = False

    top_y = 300
    bottom_y = 450

    score = 0
    game = True

    while game and score < 300:
        score += 0.123
        rel_x = min(abs(player_x - obstacle_one_x), abs(player_x - obstacle_two_x))
        abs_x = min(obstacle_one_x, obstacle_two_x)
        #rel_x = (obstacle_one_x - player_x)/800.0
        #abs_x = obstacle_one_x / 800.0

        sensors = [rel_x,abs_x, 1.0]
        output = ann.process(sensors)

        if output>0: #output positive, perform one jump
            if cycle_finished: # check if cycle is finished, then we can start a new cycle
                jump_cycle = True
                cycle_finished = False

        if jump_cycle and player_y > top_y and not reached_top: #if it has not reached the ceiling, increase velocity to go up
            player_vy = -10 + player_ay
        elif jump_cycle and reached_top: #if it's reaching the ceiling, start going down
            player_vy = 10 + player_ay

        # update player y position
        if(player_y <= bottom_y and player_y >= top_y): #if it's in bound, update it
            player_y += player_vy
        if(player_y < top_y): #if it has reached the ceiling
            player_y = top_y
            reached_top = True
        if(player_y >= bottom_y):
            player_y = bottom_y
            jump_cycle = False
            cycle_finished = True
            reached_top = False

         # create rectangle around circle and move the rectangle with the circle
        playerRect = pygame.Rect(player_x - 25, player_y - 25, 50, 50)
        obstacle_one = pygame.Rect(obstacle_one_x - 23, obstacle_one_y - 23, 45, 45)
        obstacle_two = pygame.Rect(obstacle_two_x - 23, obstacle_two_y - 23, 45, 45)

        # update obstacle x position
        obstacle_one_x -= obstacle_one_vx
        if(obstacle_one_x < 5):
            obstacle_one_x = obstacle_two_x + random.randint(400, 500)


        #obstacle two, update position
        obstacle_two_x -= obstacle_two_vx
        if(obstacle_two_x < 5):
            number = random.randint(400, 500)
            obstacle_two_x = obstacle_one_x + number

        # check if there is collision object 1
        if playerRect.colliderect(obstacle_one):
            game = False

        # check if there is collision object 2
        if playerRect.colliderect(obstacle_two):
            game = False

        if display:
            screen.fill(BLACK)
            pygame.draw.circle(screen, WHITE, (player_x, player_y), 25, 0) #draw the player
            pygame.draw.rect(screen, RED, obstacle_one, 0) # draw the obstacle
            pygame.draw.rect(screen, PRETTY_BLUE, obstacle_two, 0)
            pygame.display.update()
            clock.tick(30)

    return score



if (__name__=='__main__'):
    from dna import neuron
    ann = neuron()
    print game_function(ann)
    pygame.quit()
    sys.exit()


