#! /usr/bin/env python

import pygame
import basicSprite
from helpers import *

class Snake(basicSprite.Sprite):
        
    def __init__(self, centerPoint, image):
        """initialize base class"""
        basicSprite.Sprite.__init__(self, centerPoint, image,'SN')
        """Initialize the number of pellets eaten"""
        self.letters = 0
        """Set the number of Pixels to move each time"""
        self.x_dist = 24
        self.y_dist = 24
        self.yMove = 0;
        self.xMove = 0;
        """Initialize how much we are moving"""
        
    def MoveKey(self,key):
        if (self.xMove == 0 and self.yMove == 0):
            if (key == K_RIGHT):
                self.xMove += self.x_dist
            elif (key == K_LEFT):
                self.xMove += -self.x_dist
            elif (key == K_UP):
                self.yMove += -self.y_dist
            elif (key == K_DOWN):
                self.yMove += self.y_dist

#    def MoveKeyDown(self, key):
#        """This function sets the xMove or yMove variables that will
#        then move the snake when update() function is called.  The
#        xMove and yMove values will be returned to normal when this 
#        keys MoveKeyUp function is called."""
#        
#        if (key == K_RIGHT):
#            self.xMove += self.x_dist
#        elif (key == K_LEFT):
#            self.xMove += -self.x_dist
#        elif (key == K_UP):
#            self.yMove += -self.y_dist
#        elif (key == K_DOWN):
#            self.yMove += self.y_dist
#        
#    def MoveKeyUp(self, key):
#        """This function resets the xMove or yMove variables that will
#        then move the snake when update() function is called.  The
#        xMove and yMove values will be returned to normal when this 
#        keys MoveKeyUp function is called."""
#        
#        if (key == K_RIGHT):
#            self.xMove += -self.x_dist
#        elif (key == K_LEFT):
#            self.xMove += self.x_dist
#        elif (key == K_UP):
#            self.yMove += self.y_dist
#        elif (key == K_DOWN):
#            self.yMove += -self.y_dist
#            
