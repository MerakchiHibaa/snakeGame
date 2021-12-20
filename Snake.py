import tkinter as tk
import math
import random
import pygame
from tkinter import messagebox
#pass is just a placeholder for functionality to be added later
class cube(object):
    rows=0 
    w=0
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass

    def move(self, dirnx, dirny) :
        pass

class snake(object):
    body = []
    turns = {} # a class variable, a set
    def __init__(self, color, pos):
        self.color = color 
        self.head = cube(pos) # the new cube that the snake eats, the head is the starting position at first then it mves according to the position
        # The append() method adds an item to the end of the list.
        self.body.append(self.head) #add thhe head to the body
        # the directions can only be 1 or -1 or 0 id x=0 then y=1 cuz it can only move in one direction at the same time
        self.dirnx = 0
        self.dirny = 1


    def move(self):
        for event in pygame.even.get() :
            if event.type == pygame.QUIT:
                pygame.quit()
            keys =  pygame.key.geet_pressed() #returns a list of all the keys and if they are pressed or not
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx= -1
                    self.dirny =0 
                    self.turns[self.head.pos[:]]= [self.dirnx, self.dirny]
                elif keys[pygame.K_RIGHT]:
                    self.dirnx= 1
                    self.dirny =0 
                    self.turns[self.head.pos[:]]= [self.dirnx, self.dirny]
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        for i,c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                move(turn[0])

    def resert(self, pos):
        pass 
    def addCube(self) :
        pass
    def draw(self, surface) : 
        pass 
def drawGrid(w, rows, surface):
    sizeBtwn = w // rows #floor division, rounds the result down to the nearest whole number
    #size between the rows= width / rows
    x = 0
    y = 0
    for l in range(rows) : #drawing the grid for every row draw a line
        x = x+ sizeBtwn
        y = y+ sizeBtwn
        pygame.draw.line(surface , (255,255,255) , (x,0) , (x,w))
        pygame.draw.line(surface , (255,255,255) , (0,y) , (w,y))

    
def redrawWindow(surface):
    global rows , width
    surface.fill((0,0,0))
    drawGrid(width, rows ,surface)
    pygame.display.update()

def randomSnack(rows, items) :
    pass
def message_box(subject, content):
    pass
def main():
    global width , rows
    width = 500 
    rows = 20 
    win = pygame.display.set_mode((width, width)) #the surface that will be passed to redrawwindow
    s = snake((255,0,0) , (10,10)) # color, position
    flag = True
    clock = pygame.time.Clock()
    while flag: 
        pygame.time.delay(50) #delay 50ms so the snake wont run too fast
        clock.tick(10) #the snake will run 10 frames per second
        redrawWindow(win) 
#cube.rows = rowscube.w = w
main()
