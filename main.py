from AsteroidManager import AsteroidManager
import pygame
import time
from pygame.locals import *

from pygame.constants import FULLSCREEN, K_DOWN, K_LEFT, K_RIGHT, K_UP, K_SPACE
 
import Background
import Character
import Engine
import PlatformsManager
import Cloud
import AsteroidManager

WIDTH = 2000
HEIGHT = 1300
TICK = 60

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT], RESIZABLE)

character = Character.Character()
background = Background.Background()
platformsManager = PlatformsManager.PlatformsManager()
cloud = Cloud.Cloud()
asteroidManager = AsteroidManager.AsteroidManager()

character.int(screen, platformsManager, cloud, asteroidManager)
background.int(WIDTH, HEIGHT, screen, character)
platformsManager.int(10, screen, character)
cloud.int(screen, character)
asteroidManager.int(10, screen, character)

tickUpdates = []
tickUpdates.append(background.update)
tickUpdates.append(platformsManager.update)
tickUpdates.append(character.update)
tickUpdates.append(cloud.update)
tickUpdates.append(asteroidManager.update)

k_up = False
k_left = False
k_right = False
k_down = False

start = False

for update in tickUpdates:
        update()

myFont = pygame.font.SysFont("Times New Roman", 90)
diceDisplay = myFont.render("Press Key to Start", 1, (255,0,0))
screen.blit(diceDisplay, (WIDTH/2 - 320, HEIGHT/2))



while not start:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            start = True
        if event.type == pygame.QUIT:
            exit()

running = True
while running:
    start = time.time() * 1000
    screen.fill((0, 0, 0)) #Set pygame background black so any missing areas of images are black and not previous/random colors 

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP or event.key == K_SPACE:
                k_up = True
            if event.key == K_LEFT:
                k_left = True
                character.xAcc -= 15
            if event.key == K_RIGHT:
                k_right = True
                character.xAcc += 15
            if event.key == K_DOWN:
                k_down = True

        if event.type == pygame.KEYUP:
            if event.key == K_UP or event.key == K_SPACE:
                k_up = False
                character.stopJump()
            if event.key == K_LEFT:
                k_left = False
                character.xAcc += 15
            if event.key == K_RIGHT:
                k_right = False
                character.xAcc -= 15
            if event.key == K_DOWN:
                k_down = False

        if event.type == pygame.QUIT:
            running = False

    if k_up:
        pass
        character.jump()
    if k_left:
        pass
    if k_right:
        pass
    if k_down:
        pass
   
    for update in tickUpdates:
        update()


    pygame.display.flip()
    end = time.time() * 1000
    delay = int(1000/TICK - (end - start))
    pygame.time.delay(delay)

    