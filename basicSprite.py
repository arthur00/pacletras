#! /usr/bin/env python

import pygame

class Sprite(pygame.sprite.Sprite):
        
    def __init__(self, centerPoint, image, letter):
        pygame.sprite.Sprite.__init__(self) 
        """Set the image and the rect"""
        self.image = image
        self.rect = image.get_rect()
        """Move the rect into the correct position"""
        self.rect.center = centerPoint
        self.letter = letter;
        
    def update(self,block_group):
        """Called when the Snake sprit should update itself"""
        self.rect.move_ip(self.xMove,self.yMove)
        """IF we hit a block, don't move - reverse the movement"""
        if pygame.sprite.spritecollide(self, block_group, False):
            self.rect.move_ip(-self.xMove,-self.yMove)
        self.xMove=0;
        self.yMove=0;