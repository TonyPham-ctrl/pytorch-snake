import pygame
import sys

pygame.init()
#Variable declaration
screenWidth = 600
screenHeight = 600
framerate = 60

xPos = 200
yPos = 250

#create a green of size screenWidth and screenHeight
screen = pygame.display.set_mode((screenWidth, screenHeight))
#clock needed to make game speed consistent across all devices
clock = pygame.time.Clock()


#create a 'surface' in the game and set colour to blue
snake = pygame.Surface((100,200))
snake.fill('blue')

#set position
test_rect = snake.get_rect(center = (300,300))


#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(pygame.Color('green'))
    yPos -=1
    pygame.draw.rect(screen, pygame.Color('red'),test_rect)
    screen.blit(snake,test_rect)
    pygame.display.update()
    clock.tick(framerate)

