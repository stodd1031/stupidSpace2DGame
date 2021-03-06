import pygame
import random

class Plateform:
    def int(self, posX, posY, screen, character, platformsManager):
        self.width = random.randint(80, 200)
        self.height = 70
        #0.496551724 height to width ratio
        self.X = posX
        self.Y = posY
        self.left = self.X
        self.right = self.X + self.width
        self.top = self.Y
        self.bottom = self.Y + self.height
        self.IMG = pygame.image.load('./Images/platform.png')
        self.IMG = pygame.transform.scale(self.IMG, (self.width,self.height))
        self.point = True

        self.screen = screen
        self.screenHeight = screen.get_height()
        self.character = character
        self.platformsManager = platformsManager

    def update(self):
        if self.character.Y < int(2/5 * self.screenHeight):
            self.Y += (int(2/5 * self.screenHeight) - self.character.Y)
            self.top = self.Y
            self.bottom = self.Y + self.height

        if self.Y > self.screenHeight:
            me = self.platformsManager.getPlatform(self)
            self.Y = random.randint(self.platformsManager.platforms[me - 1].Y - self.screen.get_height()/2, self.platformsManager.platforms[me - 1].Y - self.screen.get_height()/4)
            self.point = True
            self.width = random.randint(80, 200)
            self.IMG = pygame.transform.scale(self.IMG, (self.width,self.height))
            self.right = self.X + self.width
            self.left = self.X
            self.platformsManager.visiblePlatforms.remove(self)
            self.top = self.Y
            self.bottom = self.Y + self.height
        elif self.bottom > 0:
            if not self in self.platformsManager.visiblePlatforms:
                self.platformsManager.visiblePlatforms.append(self)
            

        
        self.screen.blit(self.IMG, (self.X, self.Y))

