import pygame
import numpy as np
import time
import os
from random import randint

W = 22
H = 22
width = 200
height = 200
green = (0, 100, 0, 255)
black = (0, 0, 0)

def total_area(board, x, y):
    top = board[y - 1][x - 1] + board [y - 1][x] + board[y -1][x + 1]
    side = board[y][x - 1] + board[y][x + 1]
    bottom = board[y + 1][x - 1] + board [y + 1][x] + board[y + 1][x + 1]
    #print("cell (" + str(board[y][x]) + ") " +str(x) + "," + str(y) +" = " + str(top + side + bottom))
    return(top + side + bottom)

def spawn(board, x, y):
    board[y][x] = 1

def despawn(board, x ,y):
    board[y][x] = -1

def check_cell(board, stage, x, y):
    total = total_area(board, x, y)
    if board[y][x] == 0 and total == 3:
        #print("SPAWN!!")
        spawn(stage, x, y)
    elif board[y][x] == 1 and total > 3:
        despawn(stage, x, y)
    elif board[y][x] == 1 and total < 2:
        despawn(stage, x, y)
    else:
        return

def print_board(board, screen):
    for row in range(1, H-1):
        for col in range(1, W - 1):
            if board[row][col] == 1:
                print ('X', end='')
                #pygame.draw.circle(screen, green, (col*15 - 10, row*15 - 10), 7)
                #pygame.draw.rect(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), (col*10 - 10, row*10 - 10, 10, 10))
                pygame.draw.rect(screen, (100,0,0),(col*10 - 10, row*10 - 10, 10, 10))
            else:
                print (' ', end='')
        print(' ')
    pygame.display.flip()

def check_board(board):
    x = 1
    y = 1
    stage = np.zeros((H,W), dtype=int)
    while y < H-1:
        while x < W-1:
            #print ("Checking " + str(x) + "," + str(y))
            check_cell(board, stage, x, y)
            x += 1
        x = 1
        y += 1
    board += stage

def frame_wipe(board, screen):
    os.system("clear")
    check_board(board)
    print_board(board, screen)

def display_init():
    pygame.display.init()
    screen = pygame.display.set_mode((width, height))
    return(screen)


def main():
    board = np.zeros((H,W), dtype=int)
    spawn(board, 9, 9)
    spawn(board, 7, 10)
    spawn(board, 8, 10)
    spawn(board, 9, 10)
    spawn(board, 10, 11)
    spawn(board, 10, 11)
    spawn(board, 11, 12)
    screen = display_init()
    print_board(board, screen)
    for i in range(60):
        frame_wipe(board, screen)
        time.sleep(.5)
        screen.fill(black)
    exit(0)
main()
