import pygame
import math as m
import random
from pygame.locals import *

pygame.init()
w,h = 600,700;
#initialize screen
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Space invader")
clock=pygame.time.Clock()

#loaing images
player = pygame.image.load("pygame imgs/ship1.png")
player = pygame.transform.scale(player ,(70,70))

bullet = pygame.image.load("pygame imgs/bullet1.png")
bullet = pygame.transform.scale(bullet ,(40,40))

go = pygame.image.load("pygame imgs/go.jpg")
go = pygame.transform.scale(go ,(w,h))




bg = pygame.image.load("pygame imgs/bg.jpg")

def message(text,x,y):
    font = pygame.font.SysFont(None ,50)
    msg = font.render(text ,True, (255,255,255))
    screen.blit(msg ,(x ,y))


def set(img ,x,y):
    screen.blit(img ,(x,y))

def change_positions():
    x = random.randint(65,w-65)   
    y= random.randint(10 ,h-250)

    return x,y
 

    
#gameloop function
def gameloop():

    enemy=[]
    enemy_x=[]
    enemy_y=[]
    enemy_v = []

    no_of_enemies=6

    for i in range(no_of_enemies):
        enemy.append(pygame.image.load("pygame imgs/enemy1.png"))
        enemy_x.append(random.randint(65,w-65) )
        enemy_y.append(random.randint(10,h-250) )
        enemy_v.append(2)


    over = False
    score = 0
#game variabels 
    player_x=300
    player_y =550
    player_v=0

    bullet_x=player_x+21
    bullet_y=player_y+10

    bullet_v=0

    state ="ready"
    while not over:
        screen.fill((0,0,0))
        set(bg ,0,0)

    #event handling
        for event in pygame.event.get():
                #to quit the screen while clicked on cancel
            if event.type == pygame.QUIT:
                
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_RIGHT:
                    player_v=3
                if event.key == K_LEFT:
                    player_v=-3     
                if event.key == K_UP:
                    bullet_v=-3
                    if state=="ready":
                        bullet_x=player_x+20
                    state = "fired"   

            if event.type == pygame.KEYUP:
                player_v=0

        
        player_x+=player_v

        for i in range(no_of_enemies):
            enemy_x[i]+=enemy_v[i]

            #collidion conditions
            #----------------------
            if m.sqrt(m.pow(enemy_x[i]-bullet_x ,2) + m.pow(enemy_y[i]-bullet_y ,2) )<=50:
                state ="ready"
                score+=1
                enemy_x[i] , enemy_y[i] = change_positions()
               

            if(enemy_x[i]>w-60 or enemy_x[i]<0):
                enemy_y[i]+=30
                enemy_v[i] = -(enemy_v[i])

            set(enemy[i],enemy_x[i],enemy_y[i])
            if(abs(enemy_y[i]-player_y)<=45):
                gameover()
                over = True

        if(bullet_y<0):
            bullet_y = player_y+10
            state = "ready"

        if(state=="ready"):
            bullet_x=player_x+20
            bullet_y=player_y+10
            
        if(state=="fired"):
            bullet_y+=bullet_v

        set(bullet ,bullet_x,bullet_y)

        set(player ,player_x,player_y)
        
        txt = f"Score : {score}"
        message(txt ,250,20)
        pygame.display.update()
        clock.tick(120)


def gameover():
    
    start_again = False
    
    while not start_again:
        screen.fill((0,0,0))
        txt = "Press 'S' to start again"
        for event in pygame.event.get():
                #to quit the screen while clicked on cancel
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == K_s:
                   
                    start_again = True
                    gameloop()

        set(go ,0,0)
        message(txt ,150 ,600)
        pygame.display.update()             




gameloop()