import pygame
import random
import os

pygame.mixer.init()
pygame.init()
 
 #colors
white = (255,255,255) 
black = (0,0,0)
red= (255,0,0 )
green=(0,254,0)

# gamedisplay
screen_width= 800
screen_height=600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
#bgImage
bgimg = pygame.image.load("bgimg.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width,screen_height)).convert_alpha( )

# gametitle
pygame.display.set_caption("snakkkyy")
pygame.display.update()
clock= pygame.time.Clock()
font =pygame.font.SysFont(None,40)


def text_screen(text, color, x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,red, (x,y,snake_size,snake_size))
    for x,y in snk_list[:-2]:
        pygame.draw.rect(gameWindow,black, (x,y,snake_size,snake_size))
   
def welcome():
    exit_game =False
    pygame.mixer.music.load('sounds/Welcome.mp3')
    pygame.mixer.music.play()
    while not exit_game:
        gameWindow.fill((100,210,230))
        text_screen("welcome to snake game$",red,220,270)    
        text_screen("Press space to start Game",black,214,310)    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game =True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('sounds/BGM.mp3')
                    pygame.mixer.music.play()
                    gameloop()
                
        pygame.display.update()
        clock.tick(60)

def gameloop():
    #game varoiables
    exit_game=False
    game_over=False
    snake_x=50
    snake_y=55
    velocity_x=0
    velocity_y=0
    snake_size= 10
    fps= 60
    score=0
    init_velocity = 3.5
    food_x=random.randint(15,700)
    food_y=random.randint(15,500)
    snk_list =[]
    snk_length=1
    
#check highscore file exist?
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        highscore = f.read ()
    
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(highscore))
            gameWindow.fill((250, 253, 80))
            text_screen("Game Over! press Enter to Continue",red,147,270)
            text_screen("Score:"+ str(score ) ,black,335,330)
        
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    exit_game =True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    exit_game =True
                    
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x= init_velocity
                        velocity_y=0
                        
                    if event.key == pygame.K_LEFT:
                        velocity_x= - init_velocity
                        velocity_y=0
                        
                    if event.key == pygame.K_UP:
                        velocity_y= - init_velocity
                        velocity_x=0
                        
                    if event.key == pygame.K_DOWN:
                        velocity_y=  init_velocity
                        velocity_x=0
                        
                        
            snake_x=snake_x+velocity_x    
            snake_y=snake_y+velocity_y
            if abs(snake_x - food_x)<9 and abs(snake_y -food_y)<9:
                score += 10
                food_x=random.randint(15,700)
                food_y=random.randint(15,500)
                init_velocity = init_velocity+0.2
                pygame.mixer.music.load('sounds/eating-sound-effect-36186.mp3')
                pygame.mixer.music.play()
                snk_length += 5
                if score>int(highscore):
                    highscore = score
                
                
            gameWindow.fill((160, 255, 231))
            gameWindow.blit(bgimg, (0,0))
            text_screen("Score:"+ str(score ) +"     Highscore: "+str(highscore) +"    speed:"+ str(round(init_velocity,2) ),red,7,7)
            pygame.draw.rect(gameWindow,(20, 240, 0), (food_x,food_y,snake_size,snake_size))
            
            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
           
            if len(snk_list)>snk_length:
                del snk_list[0]
                
            if head in snk_list[:-1]:
                game_over =True
                pygame.mixer.music.load('sounds/GameOver.mp3')
                pygame.mixer.music.play()
                
            if snake_x<0 or snake_x>screen_width or snake_y <0 or snake_y>screen_height:
                game_over =True
                pygame.mixer.music.load('sounds/GameOver.mp3')
                pygame.mixer.music.play()
                
            
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
        

    pygame.quit()
    quit()
# gameloop() 
welcome()