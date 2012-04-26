#! /usr/bin/env python

import levelBase
import basicSprite
from helpers import load_image

class level(levelBase.Level):
    """Level 1 of the PyMan Game"""
    
    def __init__(self):
        self.BLOCK = 1
        self.SNAKE = 2
        self.PELLET = 'END'
        self.letterA = 'A'
        self.letterAT = '2'
        self.letterB = 'B'
        self.letterC = 'C'
        self.letterCD = '1'
        self.letterD = 'D'
        self.letterE = 'E'
        self.letterF = 'F'
        self.letterG = 'G'
        self.letterH = 'H'
        self.letterI = 'I'
        self.letterJ = 'J'
        self.letterK = 'K'
        self.letterL = 'L'
        self.letterM = 'M'
        self.letterN = 'N'
        self.letterO = 'O'
        self.letterP = 'P'
        self.letterQ = 'Q'
        self.letterR = 'R'
        self.letterS = 'S'
        self.letterT = 'T'
        self.letterU = 'U'
        self.letterV = 'V'
        self.letterX = 'X'
        self.letterY = 'Y'
        self.letterW = 'W'
        self.letterZ = 'Z'

        
    
    def getLayout(self):
        return [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ,9, 9, 9, 9, 9, 9, 9, 9, 9, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\
                [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [9, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1 ,0, 1, 1, 1, 0, 1, 1, 0, 1, 9],\
                [9, 1, 0, 2,'C', 0, 0, 0, 0,'A', 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [9, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1 ,1, 1, 0, 1, 0, 1, 1, 0, 1, 9],\
                [9, 1, 0,'C', 0, 0, 1, 0, 0, 0, 1 ,0, 0, 0, 1, 0,'C', 0, 0, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1,'X', 1, 0, 1, 1, 1, 1, 1, 0, 1, 'H', 1, 1, 1, 1, 9],\
                [9, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
                [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,'O', 0, 0, 0, 0, 0, 1, 9],\
                [9, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1,'R', 1, 1, 1, 0, 1, 1, 0, 1, 9],\
                [9, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 9],\
                [9, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 9],\
                [9, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0,'R', 0, 1, 0, 0, 0, 0, 1, 9],\
                [9, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 9],\
                [9, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,'O', 0, 0, 1, 9],\
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 'END', 1, 1, 1, 9]]         
        
    def getSprites(self):
        block, rect = load_image('blocos.png')
        pellet, rect = load_image('pellet.png',-1)
        snake, rect = load_image('livro.png',-1)
        letterA, rect = load_image('A.png',-1)
        letterB, rect = load_image('B.png',-1)
        letterC, rect = load_image('C.png',-1)
        letterCD, rect = load_image('CD.png',-1)
        letterD, rect = load_image('D.png',-1)
        letterE, rect = load_image('E.png',-1)
        letterF, rect = load_image('F.png',-1)
        letterG, rect = load_image('G.png',-1)
        letterH, rect = load_image('H.png',-1)
        letterI, rect = load_image('I.png',-1)
        letterJ, rect = load_image('J.png',-1)
        letterK, rect = load_image('K.png',-1)
        letterL, rect = load_image('L.png',-1)
        letterM, rect = load_image('M.png',-1)
        letterN, rect = load_image('N.png',-1)
        letterO, rect = load_image('O.png',-1)
        letterP, rect = load_image('P.png',-1)
        letterQ, rect = load_image('Q.png',-1)
        letterR, rect = load_image('R.png',-1)
        letterS, rect = load_image('S.png',-1)
        letterT, rect = load_image('T.png',-1)
        letterU, rect = load_image('U.png',-1)
        letterV, rect = load_image('V.png',-1)
        letterX, rect = load_image('X.png',-1)
        letterY, rect = load_image('Y.png',-1)
        letterW, rect = load_image('W.png',-1)
        letterZ, rect = load_image('Z.png',-1)
        letterAT, rect = load_image('AT.png',-1)
        
        return [pellet,block,snake,letterA,letterB,letterC,letterCD,letterD,letterE,letterF,letterG,letterH,letterI,letterJ,letterK,letterL,letterM,letterN,letterO,letterP,letterQ,letterR,letterS,letterT,letterU,letterV,letterX,letterY,letterW,letterZ,letterAT]
    
    def getName(self):
        return('CACHORRO')
    
    def getPicture(self):
        figura, rect = load_image('figuras/cachorro.png',-1)
        picture = basicSprite.Sprite([640,300],figura,'IMG')
        return picture