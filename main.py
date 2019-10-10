import pygame, sys, math, random, time, Object
pygame.init()

width = 1000
height = 1000
size = width, height
fps = 1

bgColor = (83,174,232)

screen = pygame.display.set_mode(size)
icon = pygame.image.load('icon.png')
pygame.display.set_caption("Ball Demo")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
Object.setRes(width, height)

ball1 = Object.Object(screen,5,5,"ball.png")
ball2 = Object.Object(screen,2,2,"ball2.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit();
    
    #Visuals
    screen.fill(bgColor)
    ball1.move()
    
    #Mechanics
    clock.tick(fps)
    pygame.display.flip()
