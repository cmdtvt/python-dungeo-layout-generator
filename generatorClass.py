#### Code by: https://github.com/cmdtvt ####


import pygame
from pygame.locals import *
import random

tileList = []
class dungeonGenerator():
    def __init__(self,rooms):
        self.locationList = []
        self.width = 10
        self.height = 10
        self.roomcount = rooms
        self.direction = random.randrange(1,5)
        self.allowed = True

    def getDungeon(self,):
        return self.locationList
        
    def checkLocation(self,x,y):
        for i in range(len(self.locationList)):
            if self.locationList[i][0] == x:
                if self.locationList[i][1] == y:
                    return True
        return False

    def Generate(self,):
        
        self.loc_x = 20
        self.loc_y = (self.height*20) - 20
        self.cord_x = 0
        self.cord_y = self.height

        ### This is the starting tile ###
        self.locationList.append([0,self.height])

        for i in range(self.roomcount):
            self.direction = random.randrange(1,5)
            self.allowed = True
    
            if self.direction == 1: ##UP
                if (self.loc_y + 20) < 20 or self.checkLocation(self.cord_x,self.cord_y-1) == True:
                    self.allowed = False
                else:
                    self.loc_y -= 20
                    self.cord_y -= 1
                    self.locationList.append([self.cord_x,self.cord_y])
        
            if self.direction == 2: ##DOWN
                if (self.loc_y + 20) > (self.height*20) -20 or self.checkLocation(self.cord_x,self.cord_y+1) == True:
                    self.allowed = False
                else:
                    self.loc_y += 20
                    self.cord_y += 1
                    self.locationList.append([self.cord_x,self.cord_y])

        
            if self.direction == 3: ## LEFT
                if (self.loc_x - 20) < 20 or self.checkLocation(self.cord_x-1,self.cord_y) == True:
                    self.allowed = False
                else:
                    self.loc_x -= 20
                    self.cord_x -= 1
                    self.locationList.append([self.cord_x,self.cord_y])
        
            if self.direction == 4: ## RIGHT
                if (self.loc_x + 20) > (self.width*20) or self.checkLocation(self.cord_x+1,self.cord_y) == True:
                    self.allowed = False
                else:
                    self.loc_x += 20
                    self.cord_x += 1
                    self.locationList.append([self.cord_x,self.cord_y])

class tile():
    def __init__(self,x,y,blockid):
        self.x = x
        self.y = y
        self.id = blockid

    def updatePos(self,x,y):
        self.x += x
        self.y += y

    def setPos(self,x,y):
        self.x = x
        self.y = y

    def Draw(self,screen):
        if self.id == 0:
            pygame.draw.rect(screen, (72, 73, 73),(self.x,self.y,20,20))
        if self.id == 1:
            pygame.draw.rect(screen, (159, 163, 168),(self.x,self.y,20,20))
            pygame.draw.rect(screen, (214, 10, 58),(self.x,self.y,20,20),1)

class roomGenerator():
    def __init__(self,x,y):
        self.file = open("assets/rooms/room1.level", "r")
        self.data = self.file.read().split('\n')
        self.loc_x = x
        self.loc_y = y
        self.loc_x_start = self.loc_x
        self.loc_y_start = self.loc_y
        
    def Generate(self,):
        global tileList
        for i in range(len(self.data)):
            letters = list(self.data[i])

            for y in range(len(letters)):
                if letters[y] == "x":
                    tileList.append(tile(self.loc_x,self.loc_y,0))
                    self.loc_x += 20

                if letters[y] == "f":
                    tileList.append(tile(self.loc_x,self.loc_y,1))
                    self.loc_x += 20
            self.loc_x = self.loc_x_start
            self.loc_y += 20

class levelGenerator():
    def __init__(self,x,y,rooms):
        self.rooms = rooms
        self.x = x
        self.y = y

    def Generate(self,):
        print("Creating layout...")
        dungeon = dungeonGenerator(self.rooms)
        dungeon.Generate()
        dungeon = dungeon.getDungeon()
        print(dungeon)
        print("Done!")
        print("Generating world for player...")

        for i in range(len(dungeon)):

            gen = roomGenerator(dungeon[i][0]*180,dungeon[i][1]*180)
            gen.Generate()

        
            

            
        print("Generated: "+str(len(dungeon))+" rooms!")
        print("Done!")

