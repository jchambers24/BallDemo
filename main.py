import pygame, sys, math, random, time, Object
pygame.init()

width = 1000
height = 1000
size = width, height
fps = 60

bgColor = (83,174,232)

screen = pygame.display.set_mode(size)
icon = pygame.image.load('icon.png')
pygame.display.set_caption("Ball Demo")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
Object.setRes(width, height)
#Object.Object(Surface, xVel, yVel, img, initPos, weight)
ball1 = Object.Object(screen,6,2,"ball.png",(300,300),1)
ball2 = Object.Object(screen,1,5,"ball2.png",(50,50),2)
square1 = Object.Object(screen,6,5,"square1.png",(100,100),3)
square2 = Object.Object(screen,9,4,"square2.png",(500,500),4)
penta1 = Object.Object(screen,3,4,"penta1.png",(600,600),5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit();
    
    #Objects
    screen.fill(bgColor)    
    objects = Object.getObjects()
    for obj in objects:
        obj.move()

    #Pygame
    clock.tick(fps)
    pygame.display.flip()
