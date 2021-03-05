from Platform import Plateform
import pygame
import Engine
import time

class Character:
    def int(self, screen, platformsManager, cloud):
        self.width = 87
        self.height = 150
        #0.980599647 height to width ratio
        self.X = screen.get_width()/2
        self.Y = 500 - self.height
        self.xAcc = 0
        self.yAcc = 0
        self.bottom = self.Y + self.height
        self.top = self.Y
        self.left = self.X
        self.right = self.X + self.width
        self.IMG = pygame.image.load('./Images/png/Idle (1).png')
        self.IMG = pygame.transform.scale(self.IMG, (self.width,self.height))
        self.jumping = False
        self.jumpAllowed = True
        self.points = 0

        self.myFont = pygame.font.SysFont("Times New Roman", 50)
        

        self.screen = screen
        self.screenHeight = self.screen.get_height()
        self.platformsManager = platformsManager
        self.cloud = cloud


    def update(self):
        if self.Y < int(2/5 * self.screenHeight):
            self.Y = int(2/5 * self.screenHeight)


        
        self.X += self.xAcc
        self.Y += self.yAcc

        self.left = self.X
        self.right = self.X + self.width
        self.top = self.Y
        self.bottom = self.Y + self.height

        if self.top > self.cloud.top:
            self.endGame()

        if self.bottom >= self.screen.get_height():
            self.endGame()
            # self.jumpAllowed = True
            # self.Y = self.screen.get_height() - self.height
            # self.yAcc = 0
        else:
            self.jumpAllowed = False
            self.yAcc += 2
            pass

        for platform in self.platformsManager.platforms:
            side = Engine.sideCollision(self, platform)

            if side == 'bottom':
                self.jumpAllowed = True
                self.Y = platform.top - self.height
                self.yAcc = 0
                if platform.point:
                    self.points += 1
                    platform.point = False
                    self.diceDisplay = self.myFont.render(str(self.points), 1, (255,0,0))
                    #print(self.points)
            if side == 'top':
                self.jumping = False
                self.jumpAllowed = False
                self.Y = platform.bottom
            if side == 'left':
                self.X = platform.right + 1
            if side == 'right':
                self.X = platform.left - self.width - 1

        self.screen.blit(self.IMG, (self.X, self.Y))
        self.screen.blit(self.diceDisplay, (self.screen.get_width()/2 - 100, 30))
        #self.screen.blit(self.BOTTOM, (self.X, self.bottom))


        if self.jumping and self.jumpAllowed:
            self.yAcc -= 50
        if not self.jumping and not self.jumpAllowed:
            self.yAcc = 35
    
    def endGame(self):
        myFont = pygame.font.SysFont("Times New Roman", 90)
        diceDisplay = myFont.render("Game Over", 1, (255,0,0))
        self.screen.blit(diceDisplay, (self.screen.get_width()/2 - 200, self.screen.get_height()/2))
        pygame.display.flip()
        pygame.time.delay(5000)
        exit()
