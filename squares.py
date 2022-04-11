import pygame

GRAY = (150,150,150)

class Square(pygame.sprite.Sprite):
  # Constructor function
  def __init__(self, x, y, row, column):
    super().__init__()
    self.image = pygame.Surface([50,50])
    self.image.fill(GRAY)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.index = [row,column]