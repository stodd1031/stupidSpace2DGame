import random
import pygame

class Asteroid:
    def int(self, x, y, character, screen, asteroidManager):
        self.width = random.randint(50, 200)
        self.height = random.randint(50, 200)
        self.X = x
        self.Y = y
        self.xAcc = random.randint(-10, 10)
        self.left = self.X
        self.right = self.X + self.width
        self.top = self.Y
        self.bottom = self.Y + self.height

        self.IMG = pygame.image.load('./Images/asteroid.png').convert_alpha()
        self.IMG = pygame.transform.scale(self.IMG, (self.width,self.height))

        self.character = character
        self.screen = screen
        self.asteroidManager = asteroidManager


    def update(self):
        if self.character.Y < int(2/5 * self.screen.get_height()):
            self.Y += (int(2/5 * self.screen.get_height()) - self.character.Y)
            self.top = self.Y
            self.bottom = self.Y + self.height

        if self.top > self.screen.get_height():
            me = self.asteroidManager.getAsteroid(self)
            previous = self.asteroidManager.asteroids[me - 1]
            self.X = random.randint(0, self.screen.get_width())
            self.Y = random.randint(previous.Y - 1000, previous.Y - 500)
            self.width = random.randint(50, 200)
            self.height = random.randint(50, 200)
            self.IMG = pygame.transform.scale(self.IMG, (self.width,self.height))
            self.asteroidManager.visibleAsteroids.remove(self)
            self.right = self.X + self.width
            self.left = self.X
            self.top = self.Y
            self.bottom = self.Y + self.height
        elif self.bottom > 0:
            if not self in self.asteroidManager.visibleAsteroids:
                self.asteroidManager.visibleAsteroids.append(self)
            self.X += self.xAcc
            self.left = self.X
            self.right = self.X + self.width

        self.screen.blit(self.IMG, (self.X, self.Y))

    def newLocation(self):
        pass