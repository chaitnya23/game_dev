import pygame
import random 

pygame.init()


clock=pygame.time.Clock()

#ui screen measurements ,asset img measurements
width = 300
height = 600

bird_size = 40
pipe_heigth = 400
pipe_width = 60

screen = pygame.display.set_mode((width ,height))

#images-loading states
bg = pygame.image.load('asset/background_img.jpg')
bg = pygame.transform.scale(bg ,(width,height))

bird = pygame.image.load('asset/bird.png')
bird = pygame.transform.scale(bird ,(bird_size ,bird_size))

pipe1 = pygame.image.load('asset/pipe.png')
pipe1 = pygame.transform.scale(pipe1 ,(pipe_width ,pipe_heigth))

pipe2 = pygame.transform.rotate(pipe1 , 180)
# game vars

bg_v = 0
bg_x=0


#functions
def set_img(var ,x,y):
    screen.blit(var ,(x,y))

#crete obstacal
def create_obstacal():

    pipe2_pos = random.randint(-300 ,0)
    gap = random.randint(80 ,190)
    pipe1_pos = pipe_heigth+pipe2_pos+gap

    return pipe1_pos ,pipe2_pos 


def isCrashed(p_x,p_y,pipe_x,pipe_height ,pipe_y):

    if (p_y<pipe_height) and abs(pipe_x-p_x)<=bird_size-5:
        return True
    if(pipe_height==0):
        if abs(pipe_x-p_x)<=bird_size-5 and p_y+bird_size>=pipe_y:
            return True

    return False
      

    



#game loop
def run_game():
    
    #game vars
    game_over = False
    bg_v = 0
    bg_x=0
    bird_x = 100
    bird_y = 300
    bird_v = 0
    pipe_x = width+50

    pipe1_pos=400
    pipe2_pos = -100


    pipe_v = 0


    screen.fill((0,0,0))
    set_img(bg ,0,0)
    set_img(bg ,width ,0)
    


    while not game_over:
        
    #event handling
        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_SPACE:
                    bg_v = 1
                    pipe_v=1

                if event.key == pygame.K_UP:
                    bird_v =-2

            if event.type == pygame.KEYUP:
                bird_v = 1

        
        #moving background
        bg_x-=bg_v
        set_img(bg ,bg_x,0)
        set_img(bg ,width+bg_x ,0)       

        if(bg_x<=-width):
            set_img(bg ,width ,0)
            bg_x=0

        #bird motion
        bird_y+=bird_v
        set_img(bird ,bird_x ,bird_y)

        #pipes motion 
        pipe_x-=pipe_v
        set_img(pipe2 ,pipe_x,pipe2_pos)
        set_img(pipe1 ,pipe_x,pipe1_pos)


        if(pipe_x<=-20):
            pipe1_pos ,pipe2_pos = create_obstacal()
            pipe_x = width+100

        if isCrashed(bird_x ,bird_y ,pipe_x  ,pipe_heigth+pipe2_pos ,0) or isCrashed(bird_x ,bird_y ,pipe_x , 0,pipe1_pos):
            game_over = True

        clock.tick(100)
        pygame.display.update()

        

run_game() 
pygame.quit()
quit()      

        
