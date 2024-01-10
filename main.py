import sys

import pygame
from pygame.locals import QUIT

pygame.init()


# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
x= 50
y= 50
#added Velocity to make player movment easer
vel=5



# Display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption('GAME')

sprite_sheet_image = pygame.image.load('sprites/doux.png').convert_alpha()

# Background color
background = (50, 50, 50)

#https://www.youtube.com/watch?v=M6e3_8LHc7A&list=PLjcN1EyupaQmZw8C-q6a4Zekidxf8SUj3&index=3

def get_image(sheet, width, height, scale):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    
    return image

frame_0 = get_image(sprite_sheet_image, 24, 24, 10)

# Player(posX, posY, Hight, Width)
# player = pygame.Rect((300, 250, 50, 50))

# The event handler
run = True
while run:

    # refresh the screen
    screen.fill(background)
    
    screen.blit(frame_0, (0, 0))

    # draws 'player' rectangle on screen with color white
    # pygame.draw.rect(screen, (255, 255, 255), player)

    # player movement controles
    keys = pygame.key.get_pressed()
    if keys [pygame.K_w]:
       player.move_ip(0, -1)
    elif keys [pygame.K_s]:
       player.move_ip(0, 1)
    if keys [pygame.K_d]:
       player.move_ip(1, 0)
    elif keys [pygame.K_a]:
       player.move_ip(-1, 0)

    # pygame event handling
    for event in pygame.event.get():

        # Checks if the close button was clicked and if so ends the game
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()