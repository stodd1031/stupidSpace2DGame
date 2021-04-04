from Platform import Plateform
import pygame
import Platform
import random

class PlatformsManager:
    def int(self, amount, screen, character):
        self.amount = amount
        self.platforms = [None] * amount
        self.visiblePlatforms = []
        for i in range(0, amount):
            if i > 0:
                randomX = random.randint((self.platforms[i-1].X)-(500), self.platforms[i-1].X + 500)
                while randomX < 0 or randomX > screen.get_width() - 80:
                    randomX = random.randint((self.platforms[i-1].X)-(500), self.platforms[i-1].X + 500)
                randomY = random.randint((self.platforms[i-1].Y)-(500), self.platforms[i-1].Y - 300)

                platform = Platform.Plateform()
                platform.int(randomX, randomY, screen, character, self)
            else:
                platform = Platform.Plateform()
                platform.int(screen.get_width()/2, 500, screen, character, self)
            
            self.platforms[i] = platform
            if platform.bottom > 0:
                self.visiblePlatforms.append(platform)
        

    def update(self):
        for i in range(0, self.amount):
            self.platforms[i].update()

    def getPlatform(self, platformLocation):
        return self.platforms.index(platformLocation)
