import pygame
from pygame import mixer
pygame.init()
mixer.init()
w=800
h=600
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("...PONG GAME...")


clock=pygame.time.Clock()

font=pygame.font.SysFont(None,40)

def text_screen(text,colour,x,y):
    screen_text=font.render(text,True,colour) #to printing the text in respective colour
    screen.blit(screen_text,[x,y])

def welcome():
    exit =False

    while not exit:
        screen.fill((0,0,0))
        text_screen("THE PONG GAME ", (0,0,255), 250, 100)
        text_screen("PRESS S TO START", (255,255,255), 250, 300)
        text_screen("PRESS Q TO QUIT", (255,255,255), 250, 350)
        text_screen("-by chaitnya", (0,255,0), 600, 500)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        gameloop()
                    if event.key == pygame.K_q:
                        exit = True
                          
        pygame.display.update()
    
def gameloop():
    w=800
    h=600
    screen = pygame.display.set_mode((w,h))
    silver=(192,192,192)
    BG_colour=(28,170,156)
    player_x=0
    player_y =0
    player2_x =0
    player2_y = 0 
    player_v =0
    ball_x =w/2
    ball_y = h/2
    ball_vx =8
    ball_vy =8
    score =0
    exit_game = False


    def drawplayer(x,y):
        pygame.draw.rect(screen, (0,0,0),[x, y, 10,120])


    def drawball(x,y):
        pygame.draw.circle(screen, (255,0,0), (x,y), 15)




    while not exit_game:
        
        screen.fill(BG_colour)
          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_v= -9
                    
                if event.key == pygame.K_DOWN:
                    player_v = 9

            if event.type == pygame.KEYUP:
                player_v = 0

        player_y = player_y+player_v 
        player2_y+=player_v
        ball_x+=ball_vx
        ball_y+=ball_vy

        pygame.draw.line(screen, (20,150,255), (w/2,0), (w/2,h))
        pygame.draw.rect(screen, (0,0,0),[player_x, player_y, 10,120])
        drawplayer(w-10, ball_y-60)
        drawball(ball_x,ball_y)

        if player_y<=0 or player_y>=h-120:
            player_v =0

        if ball_x<=0 or ball_x>=w-15:
            ball_vx = -ball_vx

        if ball_y<0 or ball_y>=h-15:
            ball_vy = -ball_vy 
        if pygame.draw.circle(screen, (255,0,0), (ball_x,ball_y), 15).colliderect(pygame.draw.rect(screen, (0,0,0),[player_x, player_y, 10,120])):
            ball_vx = -ball_vx 
            mixer.music.load('C:\\Users\\Chaitnya\\OneDrive\\Desktop\\project.py - Copy\\GUI.tuts.py\\gamepy\\Beep.mp3')
            mixer.music.play()
            score+=1
        text_screen("SCORE : "+ str(score), (255,255,255), w/2-110, 0)

        clock.tick(60)          
        pygame.display.update()        

welcome()

pygame.quit()
quit()