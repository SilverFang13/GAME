import pygame
from main import vel


#I would like to have more then one file but it may be easer to just have one.

pygame.init()

#checks if they keys are pressed. They are currently bound to the arrow keys for testing.
#and Subtracts or Adds current position by 5 which is the velocity.
#Left and right are x values up and down are y values.

class playermovements:
  @staticmethod
  def move_player():
    keys = pygame.key.get_pressed()
    if keys [pygame.K_UP]:
       -= vel
    if keys [pygame.K_DOWN]:
       += vel
    if keys [pygame.K_LEFT]:
       -= vel
    if keys [pygame.K_RIGHT]:
       += vel