import pygame

class Cloud():
    def int(self, screen, character):
        self.width = screen.get_width()
        self.height = int(self.width/1024 * 745)
        self.X = 0
        self.Y = screen.get_height() + 500
        self.yAcc = 0
        self.top = self.Y
        self.IMG = pygame.image.load('./Images/cloud2.png').convert_alpha()
        self.IMG = pygame.transform.scale(self.IMG, (self.width,self.height))
        self.count = 0

        self.screen = screen
        self.screenHeight = self.screen.get_height()
        self.character = character
        
    def update(self):
        self.count += 1
        self.Y += self.yAcc
        self.top = self.Y + self.height / 3
        if self.count % 3000 == 0:
            self.yAcc -= 5

        if self.character.Y < int(2/5 * self.screenHeight):
            self.Y += (int(2/5 * self.screenHeight) - self.character.Y)
        
        self.screen.blit(self.IMG, (self.X, self.Y))

        