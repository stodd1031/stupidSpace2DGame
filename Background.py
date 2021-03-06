import pygame

class Background:
    def int(self, WIDTH, HEIGHT, screen, character):
        self.width = WIDTH
        self.height = int(WIDTH/260 * 1625)
        self.IMG0 =  pygame.image.load('./Images/space.png')
        self.IMG0 = pygame.transform.scale(self.IMG0, (self.width,self.height))
        self.X0 = 0
        self.Y0 = 0
        self.IMG1 =  pygame.image.load('./Images/space.png')
        self.IMG1 = pygame.transform.scale(self.IMG1, (self.width,self.height))
        self.X1 = 0
        self.Y1 = (int(self.width/260 * 1625))
        self.top = 1

        self.screen = screen
        self.screenHeight = self.screen.get_height()
        self.character = character

    def update(self):
        if self.character.Y < int(2/5 * self.screenHeight):
            self.Y0 += (int(2/5 * self.screenHeight) - self.character.Y) / 3
            self.Y1 += (int(2/5 * self.screenHeight) - self.character.Y) / 3

        if self.Y0 > self.screenHeight:
            self.top = 0
        elif self.Y1 > self.screenHeight:
            self.top = 1
        if self.top == 1:
            self.Y1 = self.Y0 - self.height
        else:
            self.Y0 = self.Y1 - self.height
        
        self.screen.blit(self.IMG0, (self.X0,self.Y0))
        self.screen.blit(self.IMG1, (self.X1,self.Y1))

    