from Platform import Plateform
import pygame
import Platform
import random

class PlatformsManager:
    def int(self, amount, screen, character):
        self.amount = amount
        self.platforms = [None] * amount
        for i in range(0, amount):
            if i > 0:
                randomX = random.randint(0, screen.get_width()-50)
                randomY = random.randint((self.platforms[i-1].Y)-(550), self.platforms[i-1].Y - 100)

                platform = Platform.Plateform()
                platform.int(randomX, randomY, screen, character, self)
                self.platforms[i] = platform
            else:
                platform = Platform.Plateform()
                platform.int(screen.get_width()/2, 500, screen, character, self)
                self.platforms[i] = platform

    def update(self):
        for i in range(0, self.amount):
            self.platforms[i].update()

    def getPlatform(self, platformLocation):
        for platform in self.platforms:
            if platform == platformLocation:
                return self.platforms.index(platformLocation)
