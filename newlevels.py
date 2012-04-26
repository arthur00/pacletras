#! /usr/bin/env python

import pygame

class Newlevels:
        
    def __init__(self, name, layout, picname):
        self.name = name
        self.layout = layout
        self.picname = picname
        
    def getNome(self):
        return self.name
    
    def getPicname(self):
        return self.picname
    
    def getLayout(self):
        return self.layout