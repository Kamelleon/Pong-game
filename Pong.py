import sys
import pygame
import random
from pygame.locals import *
pygame.init()
WIDTH=800
HEIGHT=600
pygame.display.set_mode((WIDTH,HEIGHT))
game_display=pygame.display.get_surface()


player1=pygame.Surface((80,10))
player2=pygame.Surface((80,10))
player2.fill((255,255,255))
player1.fill((255,255,255))
pXY = player1.get_rect()
p2XY=player1.get_rect()
p2XY.x=400
p2XY.y=550
pXY.x=400
pXY.y=50

ball = pygame.image.load('ball.png')
bXY = ball.get_rect()
bXY.x=200
bXY.y=400

bx,by=3,3
px=0
pkt=0
pkt2=0
px2=0
font=pygame.font.Font("./ariendezze.ttf",40)
def p1_win():
    tekst = font.render(str(pkt),True,(255,255,255))
    tXY = tekst.get_rect()
    tXY.center=(100,40)
    game_display.blit(tekst,tXY)

def p2_win():
    text = font.render(str(pkt2),True,(255,255,255))
    t2XY = text.get_rect()
    t2XY.center=(100,500)
    game_display.blit(text,t2XY)



pygame.display.flip()

fps=pygame.time.Clock()

while True:
    game_display.fill((128,128,128))
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type==KEYDOWN:
            if event.key == K_RIGHT:
                px=5
        if event.type==KEYDOWN:
            if event.key == K_LEFT:
                px=-5
        if event.type==KEYDOWN:
            if event.key == K_DOWN:
                px=0
        if event.type == KEYDOWN:
            if event.key==K_d:
                px2=5
        if event.type == KEYDOWN:
            if event.key==K_a:
                px2=-5
        if event.type == KEYDOWN:
            if event.key==K_s:
                px2=0
    if pXY.x==0:
        px=0
        pXY.x=2

    pXY.x+=px
    bXY.x+=bx
    if pXY.colliderect(bXY):
        by=3
        bx=random.randint(3,8)
    if p2XY.colliderect(bXY):
        by=-3

    p2XY.x+=px2

    game_display.blit(player2,p2XY)

    game_display.blit(player1,pXY)


    if bXY.x>750 or bXY.x<-12:
        bx*= -1
    bXY.y+=by
    if bXY.y>550:
        by*= -1
        pkt+=1


    if bXY.y<-12:
        pkt2+=1


        by*=-1
        if pkt<0:
            pkt=0
    if pXY.x>720:
        pXY.x=719.9
    elif pXY.x<0:
        pXY.x=0.1
    if p2XY.x>720:
        p2XY.x=719.9
    elif p2XY.x<0:
        p2XY.x=0.1
    game_display.blit(ball,bXY)
    p1_win()
    p2_win()
    pygame.display.update()
    fps.tick(60)
