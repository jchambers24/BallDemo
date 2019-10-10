import pygame
resolution = [0,0]
objects = []


def setRes(x=500,y=500):
    resolution[0] = x
    resolution[1] = y

def getObjects():
    return objects

class Object:
    def __init__(self, screen, velX=5, velY=5, img="ball1.png"):
        self.screen = screen
        self.velX = velX
        self.velY = velY
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        objects.append(self)
    
    def move(self):
        moveOnAxis(self, self.velX, 0)
        moveOnAxis(self, 0, self.velY)
        self.screen.blit(self.img, self.rect)
        
    
    def moveOnAxis(self, dx, dy):

        self.rect.x += dx
        self.rect.y += dy
        for obj in getObjects():
            if self.rect.colliderect(obj.rect) and self != obj:
                if dx > 0: #Right Side Collision
                    self.rect.right = obj.rect.left 
                if dx < 0: #Left Side Collision
                    self.rect.left = obj.rect.right
                if dy > 0: #Bottom Side Collision
                    self.rect.bottom = wall.rect.top
                if dy < 0: #Top Side Collision
                    self.rect.top = wall.rect.bottom
            
