#! /usr/bin/env python
# -*- coding: latin-1 -*-
from helpers import *
from pygame.locals import *
from snakeSprite import Snake
from random import Random
import os, sys
import pygame
import newlevels
import dircache
import level001
import level002
import level003
import level004
import level005
import level006
import level007
import level008
import level009
import level010
import levelBase
import basicSprite

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

BLOCK_SIZE = 24;
        
    
class LabirintoMain:
    """The Main Class - This class handles the main 
    initialization and creating of the Game."""

    def __init__(self, width=800,height=600):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width 
                                               , self.height))
        
        pygame.display.set_mode((self.width,self.height), pygame.FULLSCREEN)
        if (self.Loadlevels() == 0):
            print 'Erro lendo levels extras'
        self.pontos = 0;
        self.cheat = 0
        self.redraw = 0;
        self.img_list = self.getImages()
        pygame.key.set_repeat(100, 20)
        
    
    def MainLoop(self):
        """This is the Main Loop of the Game"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))
        
        self.LoadIntro()
        self.Instrctions()
        self.Loadfundo()
        """
        back, rect = load_image('FUNDO1.png',-1)
        back_sprite = pygame.sprite.Group()
        backg = basicSprite.Sprite([400,300],back,'BAK')
        back_sprite.add(backg)
        back_sprite.draw(self.background)
        """
        """Load All of our Sprites"""
        if (self.cheat==1 and self.maxlevels>10):
            self.cur_level = 11;
            self.LoadSprites(11);
        else:
            self.cur_level = 1;
            self.LoadSprites(1)
        cur_letter = 0;
        finished = 0;
        """Create the background"""
        """Draw the blocks onto the background, since they only need to be 
        drawn once"""
        self.block_sprites.draw(self.background)
        self.figura_sprites.draw(self.background)
        
        while 1:
            pygame.time.delay(70)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.snake.MoveKey(event.key)
                        if (self.redraw==2):
                            self.redraw=1;
                    if (event.key == K_q):
                        sys.exit()
            """Update the snake sprite"""        
            self.snake_sprites.update(self.block_sprites)
                        
            """Check for a snake collision/pellet collision"""
            
            lstCols = pygame.sprite.spritecollide(self.snake
                                                 , self.alphabet_sprites
                                                 , True)
            end = pygame.sprite.spritecollide(self.snake
                                              , self.pellet_sprites
                                              , True)
            """Update the amount of pellets eaten"""
            
            
            if (len(lstCols) > 0):
                if ((self.snake.rect.center==lstCols[0].rect.center)):
                    if lstCols[0].letter != self.letters[cur_letter]:
                        self.pontos = self.pontos - 10;
                        self.redraw = 2;
                        wrongletter = lstCols[0]
                    else:
                        self.pontos = self.pontos + 100
                        collide = basicSprite.Sprite([self.xcolpos,570], lstCols[0].image,'COL')
                        self.alphabet_csprites.add(collide)
                        self.xcolpos += 30;
                        if cur_letter < len(self.letters):
                            if cur_letter!=len(self.letters)-1:
                                cur_letter = cur_letter+1;
                            else:
                                cp = self.fim.rect.center
                                self.pellet_sprites.remove(self.fim)
                                fima, rect = load_image('fima.png',-1)
                                fimasp = basicSprite.Sprite(cp,fima,'END')
                                self.pellet_sprites.add(fimasp)
                else:
                    self.alphabet_sprites.add(lstCols[0])

            if (len(end) > 0):
                if (self.snake.rect.center==end[0].rect.center):
                    self.background.fill((0,0,0))
                    self.pellet_sprites.empty()
                    self.snake_sprites.empty()
                    self.alphabet_sprites.empty()
                    self.alphabet_csprites.empty()
                    self.figura_sprites.empty()
                    self.block_sprites.empty()
                    if cur_letter == len(self.letters)-1:
                        self.cur_level = self.cur_level+1
                    else:
                        self.Loadfundo()
                        self.screen.blit(self.background, (0, 0))     
                        z=0;
                        if self.pontos > 0:
                            self.pontos = self.pontos - (len(self.letters)+1)*100;
                        if pygame.font:
                            font = pygame.font.Font('font.ttf', 24)
                            text = font.render("Voce não terminou de preencher as letras!",1, (255, 0, 0))
                            text2 = font.render("Pressione Qualquer Tecla Para Reiniciar a Fase",1, (255, 0, 0))
                            textpos = text.get_rect(centerx=self.background.get_width()/2)
                            textpos.centery += 10
                            textpos2 = text.get_rect(centerx=self.background.get_width()/2)
                            textpos2.centerx = textpos.centerx + 10
                            textpos2.centery = textpos.centery + 500
                            self.screen.blit(text, textpos)
                            self.screen.blit(text2,textpos2)
                            
                            lost, rect = load_image('figuras/ladrao.png')
                            perdeu = basicSprite.Sprite([400,270],lost,'LS')
                            lost_group = pygame.sprite.Group(perdeu)
                            lost_group.draw(self.screen)
                            pygame.display.flip()
                            while z==0:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT: 
                                        sys.exit()
                                    elif event.type == KEYDOWN:
                                         z=1;
                    cur_letter = 0;
                    self.redraw = 0;
                    self.LoadSprites(self.cur_level)
                    self.Loadfundo()
                    self.block_sprites.draw(self.background)
                    self.figura_sprites.draw(self.background)
                else:
                    self.pellet_sprites.add(end[0])

                
            """Do the Drawing"""               
            self.screen.blit(self.background, (0, 0))     
            if pygame.font:
                font = pygame.font.Font('font.ttf', 24)
                text = font.render("Pontos %s" % self.pontos
                                    , 1, (255, 0, 0))
                textpos = text.get_rect(centerx=self.background.get_width()/2)
                textpos.centerx += 250
                self.screen.blit(text, textpos)
               
            if self.redraw==1:
                self.alphabet_sprites.add(wrongletter)
                self.redraw=0
            
            self.pellet_sprites.draw(self.screen)
            self.snake_sprites.draw(self.screen)
            self.alphabet_sprites.draw(self.screen)
            self.alphabet_csprites.draw(self.screen)
            
            pygame.display.flip()
            
    def LoadSprites(self, level):
        """Load all of the sprites that we need"""
        """calculate the center point offset"""
        
        x_offset = (BLOCK_SIZE/2)
        y_offset = (BLOCK_SIZE/2)

        """Load the level"""   
        if level == 1:
            level1 = level001.level()
            layout = level1.getLayout()
            self.letters = level1.getName()
            figura = level1.getPicture()
        elif level == 2:
            level1 = level002.level()
            layout = level1.getLayout()
            self.letters = level1.getName()
            figura = level1.getPicture()
        elif level == 3:
            level1 = level003.level()
            layout = level1.getLayout()
            self.letters = level1.getName()
            figura = level1.getPicture()
        elif level == 4:
            level1 = level004.level()
            layout = level1.getLayout()
            self.letters = level1.getName()
            figura = level1.getPicture()
        elif level == 5:
            level1 = level005.level()
            layout = level1.getLayout()
            self.letters = level1.getName()
            figura = level1.getPicture()
        elif level == 6:
            level1 = level006.level()
            layout = level1.getLayout()
            self.letters = level1.getName()
            figura = level1.getPicture()
        elif level == 7:
            level1 = level007.level()
            layout = level1.getLayout()
            self.letters = level1.getName()
            figura = level1.getPicture()
        elif level == 8:
            level1 = level008.level()
            layout = level1.getLayout()
            self.letters = level1.getName()
            figura = level1.getPicture()
        elif level == 9:
            level1 = level009.level()
            layout = level1.getLayout()
            self.letters = level1.getName()
            figura = level1.getPicture()
        elif level == 10:
            level1 = level010.level()
            layout = level1.getLayout()
            self.letters = level1.getName()
            figura = level1.getPicture()
        elif (level > 10 and level <= self.maxlevels):
            level1 = level001.level()
            layout = self.newlevels[level-11].getLayout()
            self.letters = self.newlevels[level-11].getNome()
            picture, rect = load_image(self.newlevels[level-11].getPicname(),-1)
            figura = basicSprite.Sprite([640,300],picture,'IMG')
        elif level > self.maxlevels:      
            if pygame.font:
                z = 0;
                self.background.fill((0,0,0))
                self.pellet_sprites.empty()
                self.snake_sprites.empty()
                self.alphabet_sprites.empty()
                self.alphabet_csprites.empty()
                self.figura_sprites.empty()
                self.block_sprites.empty()
                self.Loadfundo()
                self.screen.blit(self.background, (0, 0))     
                pygame.display.flip()
                font = pygame.font.Font('font.ttf', 24)
                text = font.render("Parabéns!!! Você ganhou o Jogo!!!!!", 1, (255, 0, 0))
                text2 = font.render("Pressione 'Q' Para Sair ou Qualquer Tecla para Reiniciar", 1, (255, 0, 0))
                text3 = font.render("Sua pontuação foi: %s" % self.pontos, 1, (255, 0, 0))
                textpos = text.get_rect(centerx=self.background.get_width()/2)
                textpos.centery += 10
                textpos2 = text.get_rect(centerx=self.background.get_width()/2)
                textpos2.centerx = textpos.centerx - 70
                textpos2.centery = textpos.centery + 500
                textpos3 = text3.get_rect(centerx=self.background.get_width()/2)
                textpos3.centery = textpos2.centery - 90
                
                self.screen.blit(text, textpos)
                self.screen.blit(text2, textpos2)
                self.screen.blit(text3, textpos3)
                won, rect = load_image('figuras/parabens.jpg')
                ganhou = basicSprite.Sprite([400,230],won,'LS')                
                won_group = pygame.sprite.Group(ganhou)
                won_group.draw(self.screen)
                
                pygame.display.flip()
                while z==0:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT: 
                            sys.exit()
                        elif event.type == KEYDOWN:
                            if event.key == pygame.K_q:
                                sys.exit()
                            else:
                                self.cur_level = 1;
                                level1 = level001.level()
                                layout = level1.getLayout()
                                self.letters = level1.getName()
                                figura = level1.getPicture()  
                                self.background.fill((0,0,0))
                                pygame.display.flip()
                                self.screen.blit(self.background, (0, 0))     
                                self.pontos = 0;
                                z=1;
                                
        """Create the Pellet group"""
        self.xcolpos = 30;
        self.pellet_sprites = pygame.sprite.Group()
        self.alphabet_csprites = pygame.sprite.Group()
        """Create the block group"""
        self.block_sprites = pygame.sprite.Group()
        self.alphabet_sprites = pygame.sprite.Group()
        self.figura_sprites = pygame.sprite.Group()        
        
        self.figura_sprites.add(figura)
        
    
        for y in xrange(len(layout)):
            for x in xrange(len(layout[y])):
                """Get the center point for the rects"""
                centerPoint = [(x*BLOCK_SIZE)+x_offset,(y*BLOCK_SIZE+y_offset)]
                if layout[y][x]==level1.BLOCK:
                    block = basicSprite.Sprite(centerPoint, self.img_list[1][level%6],'BL')
                    self.block_sprites.add(block)
                elif layout[y][x]==level1.SNAKE:
                        self.snake = Snake(centerPoint,self.img_list[2])
                elif layout[y][x]==level1.PELLET:
                        self.fim = basicSprite.Sprite(centerPoint, self.img_list[0],'END')
                        self.pellet_sprites.add(self.fim)
                elif layout[y][x]==level1.letterA:
                        letterA = basicSprite.Sprite(centerPoint,self.img_list[3],'A')
                        self.alphabet_sprites.add(letterA)
                elif layout[y][x]==level1.letterB:
                        letterB = basicSprite.Sprite(centerPoint,self.img_list[4],'B')
                        self.alphabet_sprites.add(letterB)
                elif layout[y][x]==level1.letterC:
                        letterC = basicSprite.Sprite(centerPoint,self.img_list[5],'C')
                        self.alphabet_sprites.add(letterC)
                elif layout[y][x]==level1.letterCD:
                        letterCD = basicSprite.Sprite(centerPoint,self.img_list[6],'1')
                        self.alphabet_sprites.add(letterCD)
                elif layout[y][x]==level1.letterD:
                        letterD = basicSprite.Sprite(centerPoint,self.img_list[7],'D')
                        self.alphabet_sprites.add(letterD)
                elif layout[y][x]==level1.letterE:
                        letterE = basicSprite.Sprite(centerPoint,self.img_list[8],'E')
                        self.alphabet_sprites.add(letterE)
                elif layout[y][x]==level1.letterF:
                        letterF = basicSprite.Sprite(centerPoint,self.img_list[9],'F')
                        self.alphabet_sprites.add(letterF)
                elif layout[y][x]==level1.letterG:
                        letterG = basicSprite.Sprite(centerPoint,self.img_list[10],'G')
                        self.alphabet_sprites.add(letterG)
                elif layout[y][x]==level1.letterH:
                        letterH = basicSprite.Sprite(centerPoint,self.img_list[11],'H')
                        self.alphabet_sprites.add(letterH)
                elif layout[y][x]==level1.letterI:
                        letterI = basicSprite.Sprite(centerPoint,self.img_list[12],'I')
                        self.alphabet_sprites.add(letterI)
                elif layout[y][x]==level1.letterJ:
                        letterJ = basicSprite.Sprite(centerPoint,self.img_list[13],'J')
                        self.alphabet_sprites.add(letterJ)
                elif layout[y][x]==level1.letterK:
                        letterK = basicSprite.Sprite(centerPoint,self.img_list[14],'K')
                        self.alphabet_sprites.add(letterK)
                elif layout[y][x]==level1.letterL:
                        letterL = basicSprite.Sprite(centerPoint,self.img_list[15],'L')
                        self.alphabet_sprites.add(letterL)
                elif layout[y][x]==level1.letterM:
                        letterM = basicSprite.Sprite(centerPoint,self.img_list[16],'M')
                        self.alphabet_sprites.add(letterM)
                elif layout[y][x]==level1.letterN:
                        letterN = basicSprite.Sprite(centerPoint,self.img_list[17],'N')
                        self.alphabet_sprites.add(letterN)
                elif layout[y][x]==level1.letterO:
                        letterO = basicSprite.Sprite(centerPoint,self.img_list[18],'O')
                        self.alphabet_sprites.add(letterO)
                elif layout[y][x]==level1.letterP:
                        letterP = basicSprite.Sprite(centerPoint,self.img_list[19],'P')
                        self.alphabet_sprites.add(letterP)
                elif layout[y][x]==level1.letterQ:
                        letterQ = basicSprite.Sprite(centerPoint,self.img_list[20],'Q')
                        self.alphabet_sprites.add(letterQ)
                elif layout[y][x]==level1.letterR:
                        letterR = basicSprite.Sprite(centerPoint,self.img_list[21],'R')
                        self.alphabet_sprites.add(letterR)
                elif layout[y][x]==level1.letterS:
                        letterS = basicSprite.Sprite(centerPoint,self.img_list[22],'S')
                        self.alphabet_sprites.add(letterS)
                elif layout[y][x]==level1.letterT:
                        letterT = basicSprite.Sprite(centerPoint,self.img_list[23],'T')
                        self.alphabet_sprites.add(letterT)
                elif layout[y][x]==level1.letterU:
                        letterU = basicSprite.Sprite(centerPoint,self.img_list[24],'U')
                        self.alphabet_sprites.add(letterU)
                elif layout[y][x]==level1.letterV:
                        letterV = basicSprite.Sprite(centerPoint,self.img_list[25],'V')
                        self.alphabet_sprites.add(letterV)
                elif layout[y][x]==level1.letterX:
                        letterX = basicSprite.Sprite(centerPoint,self.img_list[26],'X')
                        self.alphabet_sprites.add(letterX)
                elif layout[y][x]==level1.letterY:
                        letterY = basicSprite.Sprite(centerPoint,self.img_list[27],'Y')
                        self.alphabet_sprites.add(letterY)
                elif layout[y][x]==level1.letterW:
                        letterW = basicSprite.Sprite(centerPoint,self.img_list[28],'W')
                        self.alphabet_sprites.add(letterW)
                elif layout[y][x]==level1.letterZ:
                        letterZ = basicSprite.Sprite(centerPoint,self.img_list[29],'Z')
                        self.alphabet_sprites.add(letterZ)
                elif layout[y][x]==level1.letterAT:
                        letterAT = basicSprite.Sprite(centerPoint,self.img_list[30],'2')
                        self.alphabet_sprites.add(letterAT)
        """Create the Snake group"""            
        self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
    
    def LoadIntro(self):
        
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,0,0))
        self.screen.blit(self.background, (0, 0))     
        pygame.display.flip();

        letterP, rect = load_image('intro/p.png')
        letterA, rect = load_image('intro/a.png')
        letterC, rect = load_image('intro/c.png')
        letterL, rect = load_image('intro/l.png')
        letterE, rect = load_image('intro/e.png')
        letterT, rect = load_image('intro/t.png')
        letterR, rect = load_image('intro/r.png')
        letterA, rect = load_image('intro/a.png')
        letterS, rect = load_image('intro/s.png')

        intro_sprites = pygame.sprite.Group()
        letter1 = basicSprite.Sprite([160,60],letterP,'INT') 
        letter2 = basicSprite.Sprite([420,60],letterA,'INT')
        letter3 = basicSprite.Sprite([80,60],letterC,'INT')
        letter4 = basicSprite.Sprite([550,60],letterL,'INT')
        letter5 = basicSprite.Sprite([200,60],letterE,'INT') 
        letter6 = basicSprite.Sprite([660,460],letterT,'INT')
        letter7 = basicSprite.Sprite([320,460],letterR,'INT') 
        letter8 = basicSprite.Sprite([580,460],letterA,'INT')
        letter9 = basicSprite.Sprite([440,460],letterS,'INT')
        intro_sprites.add(letter1)
        intro_sprites.add(letter2)
        intro_sprites.add(letter3)
        intro_sprites.add(letter4)
        intro_sprites.add(letter5)
        intro_sprites.add(letter6)
        intro_sprites.add(letter7)
        intro_sprites.add(letter8)
        intro_sprites.add(letter9)
        
        rectlst = [rect,letter1.rect,letter2.rect,letter3.rect,letter4.rect,letter5.rect,letter6.rect,letter7.rect,letter8.rect,letter9.rect]
        
        exit = self.IntroDraw(letter1,rectlst,intro_sprites,'DOWN','NO')
        if exit == -1:
            return;
        exit = self.IntroDraw(letter2,rectlst,intro_sprites,'DOWN','LEFT')
        if exit == -1:
            return;
        exit = self.IntroDraw(letter3,rectlst,intro_sprites,'DOWN','RIGHT')
        if exit == -1:
            return;
        exit = self.IntroDraw(letter4,rectlst,intro_sprites,'DOWN','LEFT')
        if exit == -1:
            return;
        exit = self.IntroDraw(letter5,rectlst,intro_sprites,'DOWN','RIGHT')
        if exit == -1:
            return;
        exit = self.IntroDraw(letter6,rectlst,intro_sprites,'UP','LEFT')
        if exit == -1:
            return;
        exit = self.IntroDraw(letter7,rectlst,intro_sprites,'UP','RIGHT')
        if exit == -1:
            return;
        exit = self.IntroDraw(letter8,rectlst,intro_sprites,'UP','NO')
        if exit == -1:
            return;
        exit = self.IntroDraw(letter9,rectlst,intro_sprites,'UP','RIGHT')
        if exit == -1:
            return;
           
        x=0;
        while x==0:
            pygame.time.wait(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type == KEYDOWN:
                    x=1;
                    
    def IntroDraw(self,letter,rectlst,intro_sprites,vert,horz):
        angle = 90;        
        for x in range(40):
            self.screen.blit(self.background, (0, 0))     
            if ((x%10) == 0):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        sys.exit()
                    elif event.type == KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if (keys[K_LCTRL] == 0) and (keys[K_LSHIFT]==0):
                            return -1
                        elif (keys[K_LCTRL] != 0) and (keys[K_LSHIFT]!=0) and (keys[K_j]!=0):
                            self.cheat = 1;
                            return -1
                letter.image = pygame.transform.rotate(letter.image,angle)
            rect = letter.rect.inflate(5,5);
            if vert == 'UP':
                letter.rect.centery -= 5;
            elif vert == 'DOWN':
                letter.rect.centery += 5;
            if horz == 'LEFT':
                letter.rect.centerx -= 5;
            elif horz == 'RIGHT':
                letter.rect.centerx += 5;
            pygame.time.delay(40)            
            intro_sprites.draw(self.screen)
            rectlst.append(rect)
            pygame.display.update(rectlst)
            rectlst.remove(rect)
        return 1;

    def getImages(self):
        block1, rect = load_image('1.png')
        block2, rect = load_image('2.png')
        block3, rect = load_image('3.png')
        block4, rect = load_image('4.png')
        block5, rect = load_image('5.png')
        block6, rect = load_image('6.png')
        block = [block1,block2,block3,block4,block5,block6]
        fim, rect = load_image('fimv.png',-1)
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
        
        return [fim,block,snake,letterA,letterB,letterC,letterCD,letterD,letterE,letterF,letterG,letterH,letterI,letterJ,letterK,letterL,letterM,letterN,letterO,letterP,letterQ,letterR,letterS,letterT,letterU,letterV,letterX,letterY,letterW,letterZ,letterAT]

    
    def Loadlevels(self):
        extralvls = dircache.listdir('./extra_levels')
        self.maxlevels = 10;
        matrix = 0;
        fignome = '';
        self.newlevels = []
        for x in range(len(extralvls)):
            if (extralvls[x].count('.lvl')): 
                pathdir = './extra_levels/'
                pathdir += extralvls[x];
                f = open(pathdir)
                fase = f.readlines()
                if (len(fase) < 24):
                    return 0
                i=1
                
                matrix = [0]*23
                for t in range(23):
                    matrix[t] = [0] * 21
                if (fase[i-1].count('matriz')):
                    for z in range(23):
                        temp = fase[i].split(', ')
                        for y in range(21):
                            if (temp[y].isdigit()):
                                matrix[z][y] = int(temp[y])
                            else:
                                matrix[z][y] = temp[y]
                        i+=1
                    i=0;
                else:
                    print 'Erro ao carregar',extralvls[x]
                    return 0

                done = 0;    
                while(i < len(fase)):
                    if (fase[i].count('nome')):
                        temp = fase[i].split('=')
                        if (len(temp) != 2):
                            return 0
                        fignome = temp[1].strip()
                        done += 1
                        
                    elif (fase[i].count('figura')):
                        temp = fase[i].split('=')
                        if (len(temp) != 2):
                            return 0
                        figlocal = 'figuras/'
                        figlocal += temp[1].strip()
                        
                        done += 1
                    i+=1
                
                
                if (i >= len(fase) and done!=2):
                    return 0
                
                self.maxlevels += 1;
                nlevel = newlevels.Newlevels(fignome,matrix,figlocal)
                self.newlevels.append(nlevel)
            
            
        return 1
            
    def Instrctions(self):
         self.Loadfundo()
         self.screen.blit(self.background, (0, 0))     
         pygame.display.flip()
         font = pygame.font.Font ('font.ttf', 16)
         font2 = pygame.font.Font('font.ttf', 12)
         text3 = font.render ("Sobre o Jogo...", 1, (0,0,0))
         
         text4 = font2.render ("Este jogo é um projeto realizado pelos alunos Rafael D. Lucchesi e Arthur R. S. Valadares para a materia de Interfaces (MC750) da", 1, (255,0,0))
         text41 = font2.render ("Universidade Estadual de Campinas. O jogo se encontra atualmente dentro de um Pacotão de jogos realizados pela turma e disponibilizados", 1, (255,0,0))
         text42 = font2.render("a todos através do servidor Yai.", 1, (255,0,0))
         text5 = font.render ("Objetivo...", 1, (0,0,0))
         text6 = font2.render ("O jogo tenta divertir o jogador enquanto o ensina a forma correta de certas palavras. O jogador tem duas formas de passar em casa fase,", 1, (255,0,0))
         text61 = font2.render("uma tentando encontrar um caminho logico pelo labirinto e assim pegando as letras necessarias para formar a palavra e portanto vendo a", 1, (255,0,0))
         text62 = font2.render("correta grafia da palavra. Ou tentando pegar as letras na ordem da palavra o que o levará ao fim do labirinto e também o mostrará a ", 1, (255,0,0))
         text63 = font2.render("grafia correta da palavra.", 1, (255,0,0))
         text7 = font.render ("Instruções...", 1, (0,0,0))
         text8 = font2.render ("O jogo consiste de um labirinto repleto de letras e uma figura. A figura representa a palavra que o jogador deverá formar para passar ", 1, (255,0,0))
         text81 = font2.render("de uma determinada fase.O andamento do jogo é atraves das teclas direcionais do teclado. O jogador deve passar com o livro sobre as ", 1, (255,0,0))
         text82 = font2.render("letras na ordem que formam a palavra necessária. Para cada letra certa pega o jogador ganha 100 pontos e pra cada letra errada ou fora ", 1, (255,0,0))
         text83 = font2.render("de ordem o jogador perde 10 pontos. O jogador só pode sair da fase após formar corretamente a palavra necessaria senão ele perderá 100 pontos", 1, (255,0,0))
         text84 = font2.render("pontos por letra que faltou ser pega e terá q completar a mesma fase novamente. O bloco FIM indica a saída do labirinto. Caso esteje vermelho", 1, (255,0,0))
         text85 = font2.render("é sinal que a palavra não está completamente formada. Caso esteje azul é pode-se sair do labirinto para a próxima fase. A tecla Q sai do jogo", 1, (255,0,0))
         
         
         textpos3 = text3.get_rect(centerx=self.background.get_width()/2) 
         textpos3.centery += 15
         textpos4 = text4.get_rect(centerx=self.background.get_width()/2) 
         textpos4.centery = textpos3.centery + 50
         textpos41 = text41.get_rect(centerx=self.background.get_width()/2) 
         textpos41.centery = textpos4.centery + 20
         textpos42 = text42.get_rect(centerx=self.background.get_width()/2) 
         textpos42.centery = textpos41.centery + 20
         textpos5 = text5.get_rect(centerx=self.background.get_width()/2) 
         textpos5.centery = textpos42.centery + 50
         textpos6 = text6.get_rect(centerx=self.background.get_width()/2) 
         textpos6.centery = textpos5.centery + 50
         textpos61 = text61.get_rect(centerx=self.background.get_width()/2) 
         textpos61.centery = textpos6.centery + 20
         textpos62 = text62.get_rect(centerx=self.background.get_width()/2) 
         textpos62.centery = textpos61.centery + 20
         textpos63 = text63.get_rect(centerx=self.background.get_width()/2) 
         textpos63.centery = textpos62.centery + 20
         textpos7 = text7.get_rect(centerx=self.background.get_width()/2) 
         textpos7.centery = textpos63.centery + 50
         textpos8 = text8.get_rect(centerx=self.background.get_width()/2) 
         textpos8.centery = textpos7.centery + 50
         textpos81 = text81.get_rect(centerx=self.background.get_width()/2) 
         textpos81.centery = textpos8.centery + 20
         textpos82 = text82.get_rect(centerx=self.background.get_width()/2) 
         textpos82.centery = textpos81.centery + 20
         textpos83 = text83.get_rect(centerx=self.background.get_width()/2) 
         textpos83.centery = textpos82.centery + 20
         textpos84 = text84.get_rect(centerx=self.background.get_width()/2) 
         textpos84.centery = textpos83.centery + 20
         textpos85 = text85.get_rect(centerx=self.background.get_width()/2) 
         textpos85.centery = textpos84.centery + 20
    
    
         self.screen.blit(text3,textpos3) 
         self.screen.blit(text4,textpos4) 
         self.screen.blit(text41,textpos41)
         self.screen.blit(text42,textpos42)
         self.screen.blit(text5,textpos5) 
         self.screen.blit(text6,textpos6) 
         self.screen.blit(text61,textpos61) 
         self.screen.blit(text62,textpos62) 
         self.screen.blit(text63,textpos63) 
         self.screen.blit(text7,textpos7) 
         self.screen.blit(text8,textpos8) 
         self.screen.blit(text81,textpos81) 
         self.screen.blit(text82,textpos82) 
         self.screen.blit(text83,textpos83) 
         self.screen.blit(text84,textpos84) 
         self.screen.blit(text85,textpos85) 
         pygame.display.flip()
         while(1):
             pygame.time.delay(50)
             for event in pygame.event.get():
                 if event.type == pygame.QUIT: 
                     sys.exit()
                 elif event.type == KEYDOWN:
                     return;
                 
    def Loadfundo(self):
        back, rect = load_image('FUNDO1.png',-1)
        back_sprite = pygame.sprite.Group()
        backg = basicSprite.Sprite([400,300],back,'BAK')
        back_sprite.add(backg)
        back_sprite.draw(self.background)
        pygame.display.flip()
            


if __name__ == "__main__":
    MainWindow = LabirintoMain()
    MainWindow.MainLoop()
    
