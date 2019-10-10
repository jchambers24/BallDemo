import pygame, random
resolution = [0,0]
objects = []


def setRes(x=500,y=500):
    resolution[0] = x
    resolution[1] = y

def getObjects():
    return objects
    

class Object:
    def __init__(self, screen, velX=5, velY=5, img="ball1.png", initPos=(0,0), weight = 1):
        #Init and Object Creation
        print("CREATED OBJECT "+img)
        self.screen = screen
        self.velX = velX
        self.velY = velY
        self.img = pygame.image.load(img)
        self.rect = self.img.get_rect()
        self.rect.x = initPos[0]
        self.rect.y = initPos[1]
        self.weight = weight
        objects.append(self)
    
    def move(self):
        #Splits the movement on to two axis for collision detection
        self.moveOnAxis(self.velX, 0)
        self.moveOnAxis(0, self.velY)
        self.render()
    
    def render(self):
        #Blits The Object To The Screen
        self.screen.blit(self.img, self.rect)
    
    def moveOnAxis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
        #Collision with other objects
        for obj in getObjects():
            if self.rect.colliderect(obj.rect) and self != obj:
                if dx > 0: #Right Side Collision
                    self.rect.right = obj.rect.left
                    self.velX = -self.velX
                    obj.velX = -obj.velX
                if dx < 0: #Left Side Collision
                    self.rect.left = obj.rect.right
                    self.velX = -self.velX
                    obj.velX = -obj.velX
                if dy > 0: #Bottom Side Collision
                    self.rect.bottom = obj.rect.top
                    self.velY = -self.velY
                    obj.velY = -obj.velY
                if dy < 0: #Top Side Collision
                    self.rect.top = obj.rect.bottom
                    self.velY = -self.velY
                    obj.velY = -obj.velY

        #Self Wall Collision
        if self.rect.right > resolution[0]:
            self.rect.right = resolution[0]
            self.velX = -self.velX
        if self.rect.left < 0:
            self.rect.left = 0
            self.velX = -self.velX
        if self.rect.bottom > resolution[1]:
            self.rect.bottom = resolution[1]
            self.velY = -self.velY
        if self.rect.top < 0:
            self.rect.top = 0
            self.velY = -self.velY
