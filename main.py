import pygame, time, random
from squares import *

pygame.init()

screen = pygame.display.set_mode([500, 800])
pygame.display.set_caption("Tetris")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

running = True

font = pygame.font.Font(None, 50)

clock = pygame.time.Clock()

'''
# spaces = [[0,0,0,0],                                          
            [0,0,0,0], 
            [0,0,0,0]]
'''
# Make the board with values 0
spaces = []
rows, cols = (10, 8)
for i in range(rows):
  row = []
  for j in range(cols):
    row.append(0)
  spaces.append(row)

print(spaces)

print(len(spaces))

allSquares = pygame.sprite.Group()

spaces[1][2] = 1

for i in range(len(spaces)):
    for j in range(cols):
        block = Square(j*55 + 30, i * 55 + 215, i, j)

        allSquares.add(block)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(allSquares.sprites())):
                curBlock = allSquares.sprites()[i]
                if curBlock.rect.collidepoint(event.pos):
                    print (str(curBlock.index))
    screen.fill(BLACK)
    text = font.render("TETRIS", True, GREEN)
    screen.blit(text, [160, 20])
    allSquares.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()