## Simple pygame project for New Apprenticeship's IDB 10, created by Malika
## with contributions by FRANKENMILLER

import pygame
from pygame.locals import *
import random #imports random module
from pygame import mixer
## imported mixer module from pygame

size = width, height = (800, 600)
road_width = int (width/1.6)#about 60% of the screen is the grey road
roadmark_width = int (width/60)#makes 10 pixels width yellow line
right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4
speed = 1

pygame.init()
mixer.init()
## initializing both the pygame and mixer modules
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Malika's Car Game")
FONT = pygame.font.Font('freesansbold.ttf', 24)
GREEN = (60,220,0)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen.fill(BLACK)
## You can use this line to change background color of the game! The original
## value of GREEN is now a global variable, including a few new colors.
## pygame.mixer.music.load('music2.mp3')
## pygame.mixer.music.set_volume(0.3)
## pygame.mixer.music.play(-1, 0.0, 5000)##arguement[0] of -1 means infinite loop 
car_crash_fx = pygame.mixer.Sound('car_crash.wav')
car_crash_fx.set_volume(0.5)
tire_screech_fx = pygame.mixer.Sound('tire_screech.wav')
tire_screech_fx.set_volume(0.5)

instructions_line_one = FONT.render('Press left/right arrow keys to dodge on-coming traffic!', True, WHITE, BLACK)
ins_line_one_rect = instructions_line_one.get_rect()
ins_line_one_rect.center = (width//2, 25)

pygame.display.update()

#load Player images BLACK CAR
car = pygame.image.load("blackcar2.png")
car_location = car.get_rect()
car_location.center = right_lane, height*0.8


#load Enemy images WHITE CAR
car2 = pygame.image.load("whitecar2.png")
car2_location = car2.get_rect()
car2_location.center = left_lane, height*0.2

counter = 0


#GAME LOGIC LOOP
while running:

    counter += 1
    if counter == 1024:
        speed += 0.25
        counter = 0
        print ("level up", speed)



    #animate enemy image WHITECAR
    car2_location[1] += speed 
    if car2_location[1] > height:

        if random.randint(0,1) == 0: #Randomly picks which lane WHITECAR begins 
            car2_location.center =  right_lane, - 200
        else:
            car2_location.center =  left_lane, - 200

    #END GAME LOGIC
    if car_location[0] == car2_location[0] and car2_location[1] > car_location[1] - 238: #both images on same lane and white car touches black car image size
        print("Watch Out! GAME OVER")
        car_crash_fx.play()



    #EVENT LISTENERS
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False #quit game if X is clicked

        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_location =  car_location.move([- int (road_width/2), 0]) #move black car left if A key or left arrow key is pressed
                tire_screech_fx.play()
            if event.key in [K_d, K_RIGHT]:
                car_location =  car_location.move([+ int (road_width/2), 0]) #move black car right if D key or right arrow key is pressed
                tire_screech_fx.play()

                #draw graphics
    pygame.draw.rect(screen,#rectangle grey road
                    (50,50,50), #color
                    (width/2-road_width/2, 0, road_width, height )) # x cord, y cord, total width of shape, total height <--tuple

    pygame.draw.rect(screen,#middle yellow line
                     (255,240,60),
                     (width/2- roadmark_width/2, 0, roadmark_width, height))

    pygame.draw.rect(screen,#Left white line
                     (255,255,255),
                     (width/2- road_width/2 + roadmark_width*2, 0, roadmark_width, height))

    pygame.draw.rect(screen,#Right white line
                     (255,255,255),
                     (width/2 + road_width/2 - roadmark_width*3, 0, roadmark_width, height))

    screen.blit(car, car_location)
    screen.blit(car2, car2_location)
    screen.blit(instructions_line_one, ins_line_one_rect)

    pygame.display.update()


pygame.quit()
