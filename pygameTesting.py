import pygame
from sys import exit


pygame.init() # Pygame initialization
pygame.display.set_caption("Game")

screen = pygame.display.set_mode((800, 400))
fps = pygame.time.Clock()

while True:
    for event in pygame.event.get(): # Allows you to quit the screen
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # Stops the while loop, stopping the error
    # Draw all elements
    # Update everything
    pygame.display.update() # Updates screen to player
    fps.tick(60)

