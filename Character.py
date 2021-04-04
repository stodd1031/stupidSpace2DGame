from Platform import Plateform
import pygame
import Engine
import time

class Character:
    def int(self, screen, platformsManager, cloud, asteroidManager):
        self.width = 87
        self.height = 150
        self.X = screen.get_width()/2
        self.Y = 500 - self.height
        self.xAcc = 0
        self.yAcc = 0
        self.bottom = self.Y + self.height
        self.top = self.Y
        self.left = self.X
        self.right = self.X + self.width
        self.IMG = pygame.image.load('./Images/png/Idle (1).png').convert_alpha()
        self.IMG = pygame.transform.scale(self.IMG, (self.width,self.height))
        self.jumping = False
        self.jumpAllowed = True
        self.falling = False
        self.inAir = False
        self.points = 0

        self.myFont = pygame.font.SysFont("Times New Roman", 50)
        self.diceDisplay = self.myFont.render(str(0), 1, (255,255,255))

        self.screen = screen
        self.screenHeight = self.screen.get_height()
        self.platformsManager = platformsManager
        self.cloud = cloud
        self.asteroidManager = asteroidManager

    def update(self):
        if self.Y < int(2/5 * self.screenHeight):
            self.Y = int(2/5 * self.screenHeight)
            self.top = self.Y
            self.bottom = self.Y + self.height

        if self.xAcc != 0:
            self.X += self.xAcc
            self.left = self.X
            self.right = self.X + self.width
            for platform in self.platformsManager.visiblePlatforms:
                if Engine.leftCollision(self, platform):
                    self.X = platform.right + 1
                elif Engine.rightCollision(self, platform):
                    self.X = platform.left - self.width - 1
            self.left = self.X
            self.right = self.X + self.width

        self.Y += self.yAcc
        self.top = self.Y
        self.bottom = self.Y + self.height
        for platform in self.platformsManager.visiblePlatforms:
            if Engine.bottomCollision(self, platform):
                self.jumpAllowed = True
                self.falling = False
                self.jumping = False
                self.inAir = False
                self.Y = platform.top - self.height
                self.yAcc = 0
                if platform.point:
                    self.points += 1
                    platform.point = False
                    self.diceDisplay = self.myFont.render(str(self.points), 1, (255,255,255))
                break
            elif Engine.topCollision(self, platform):
                self.stopJump()
                self.Y = platform.bottom
                break
            else:
                self.inAir = True
                self.jumpAllowed = False
        self.top = self.Y
        self.bottom = self.Y + self.height
        if self.inAir:
            self.yAcc += 1

        for asteroid in self.asteroidManager.visibleAsteroids:
            if Engine.sideCollision(self, asteroid) != None:
                self.endGame()
        if self.top > self.cloud.top:
            self.endGame()
        elif self.bottom >= self.screen.get_height():
            self.endGame()
        

        self.screen.blit(self.IMG, (self.X, self.Y))
        self.screen.blit(self.diceDisplay, (self.screen.get_width()/2 - 20, 30))
    
    def endGame(self):
        myFont = pygame.font.SysFont("Times New Roman", 90)
        diceDisplay = myFont.render("Game Over", 1, (255,0,0))
        self.screen.blit(diceDisplay, (self.screen.get_width()/2 - 200, self.screen.get_height()/2))
        pygame.display.flip()
        pygame.time.delay(5000)
        exit()

    def jump(self):
        if self.jumpAllowed:
            self.yAcc -= 35
            self.jumping = True
            self.jumpAllowed = False
            self.inAir = True

    def stopJump(self):
        if self.jumping:
            self.yAcc = 0
            self.falling = True
            self.jumping = False