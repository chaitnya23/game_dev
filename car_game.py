import pygame
import random
from pygame.constants import KEYUP, K_s
pygame.init()

#screen 
w=600
h=600

#car sizes
car_width = 56
car_height =125
score =0

screen = pygame.display.set_mode((w,h)) 
clock=pygame.time.Clock()


#caption of game
pygame.display.set_caption("car race")



pygame.display.update()


bg = pygame.image.load("pygame imgs/road.png")
bg = pygame.transform.scale(bg ,(450,h))

fbg = pygame.image.load("pygame imgs/f_bg.jpeg")
fbg = pygame.transform.scale(fbg ,(w,h))

crush = pygame.image.load("pygame imgs/crashed.jpeg")
crush = pygame.transform.scale(crush ,(w,250))

player = pygame.image.load("pygame imgs/player.jpg")

#loading enemy images
e1 = pygame.image.load("pygame imgs/car2.jpg")
e2 = pygame.image.load("pygame imgs/car3.jpg")
e3 = pygame.image.load("pygame imgs/car4.jpg")
e4 = pygame.image.load("pygame imgs/player.jpg")
e5 = pygame.image.load("pygame imgs/car5.jpg")
e6 = pygame.image.load("pygame imgs/car6.jpg")

enemy = [e1 ,e2 ,e3,e4,e5,e6]

#for deploying message
def message(text,x,y):
    font = pygame.font.SysFont(None ,50)
    msg = font.render(text ,True, (0,0,0))
    screen.blit(msg ,(x ,y))


#function for setting the image at certain image
def set(var ,x,y):
    screen.blit(var ,(x,y))

enemy_v =0
enemy_x = 90
enemy_y =30
def deploye_enemy():
    for enemy_player in enemy:
        enemy_x = random.randint(85,470)
        enemy_y = random.randint(20,h-50)
        set(enemy_player ,enemy_x ,enemy_y)
      
def frontscreen():
    start = False
 
    while not start:
        set(fbg ,0,0)
        txt =" <Press 's' key to start > "
        message(txt ,150,20)
        for event in pygame.event.get():
            #to quit the screen while clicked on cancel
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_s:
                    start = True
                    game_loop()

        pygame.display.update()              
            

#game loop
def game_loop():
    l=1
    score =0
    screen.fill((119,119,119))
    crashed = False
    #velocity & position of the road ,player
    v_r=0
    car_v = 0
    car_x = 150
    pos_r=0

    #enemy positions and velocities
    enemy_v =0
    enemy_x = 140
    enemy_y = -450
    enemy_index =0

    set(bg ,70,0)
    set(bg ,70,-h)
    enemy_v = 7
    while not crashed:
        v_r=4  
   
    #event handling
        for event in pygame.event.get():
            #to quit the screen while clicked on cancel
            if event.type == pygame.QUIT:
                pygame.quit()
                crashed=True

            if event.type == pygame.KEYDOWN:
                
                if event.key==pygame.K_RIGHT:
                    car_v = 5  
                if event.key==pygame.K_LEFT:
                    car_v = -5       

            if event.type == pygame.KEYUP:
                car_v = 0

        #level improvement
        if(score>5 and score<10):
            enemy_v = 15
            l=2
           
        if(score >10 and score<20):
            enemy_v = 10
            l=3
            
        if score >25:
            enemy_v = 12 
            l=4
            

        #updating the position of car and road   and enemy vehicals     
        pos_r+=v_r
        car_x+=car_v
        enemy_y+=enemy_v
        temp = car_x

        #crashing condition
        if(car_x<=80 or car_x>=475):
            car_v = 0
            crashed = True
            after_crashed()

        if(abs(enemy_x - car_x)<= 50 and abs(enemy_y - 430)<=120):
            crashed = True
            after_crashed()
        
        #resisting the car exceeding road
        

        set(bg ,75 ,pos_r)  
        set(bg ,75,-h+pos_r) 
        if pos_r >= h:
            pos_r=0
            set(bg ,75 ,-h)
            
        if enemy_y>=h:
            enemy_x = random.randint(180,430)
            enemy_y = random.randint(-h+20,-40)
            enemy_index = random.randint(0,5)
            score+=1
            
           

        set(enemy[enemy_index] ,enemy_x,enemy_y)

        set(player ,car_x,430)
        message(f"Score : {score}" ,140,20)
        message(f"Level : {l}" ,340 ,20)
        pygame.display.update()
        clock.tick(120)




def after_crashed():
    txt = "OOps.. seems you have crashed"
    txt1 = "Press the key 'R' to start again"
    txt2 = "Press 'Q' to quit"
    start_again = False
    while not start_again:
        screen.fill((255,255,255))
        message(txt ,50,10)
        message(txt1 ,100 ,400)
        message(txt2 ,100,450)
        for event in pygame.event.get():
            #to quit the screen while clicked on cancel
            if event.type == pygame.QUIT:
                pygame.quit()
                crashed=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:    
                    game_loop()
                    start_again = True 
                    
                if event.key == pygame.K_q:
                    pygame.quit()
                    start_again = True    
        set(crush ,50 ,90)
        pygame.display.update()
        

frontscreen()
