import Asteroid
import random

class AsteroidManager:
    def int(self, amount, screen, character):
        self.amount = amount
        self.asteroids = []
        self.visibleAsteroids = []
        for i in range(0, amount):
            if i > 0:

                randomX = random.randint(0, screen.get_width())
                randomY = random.randint((self.asteroids[i-1].Y)-(1000), self.asteroids[i-1].Y - 500)

                asteroid = Asteroid.Asteroid()
                asteroid.int(randomX, randomY, character, screen, self)
            else:
                randomX = random.randint(0, screen.get_width())

                asteroid = Asteroid.Asteroid()
                asteroid.int(randomX, 0, character, screen, self)
            self.asteroids.append(asteroid)
            if asteroid.bottom > 0:
                self.visibleAsteroids.append(asteroid)


    def update(self):
        for i in range(0, self.amount):
            self.asteroids[i].update()

    def getAsteroid(self, asteroidLocation):
        return self.asteroids.index(asteroidLocation)