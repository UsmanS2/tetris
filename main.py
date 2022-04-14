import pygame, time, random, math
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



allSquares = pygame.sprite.Group()

#spaces[1][2] = 1

for i in range(len(spaces)):
    for j in range(cols):
        block = Square(j*55 + 30, i * 55 + 215, i, j)

        allSquares.add(block)

start_ticks = pygame.time.get_ticks()
seconds = 0

while running:
    seconds = math.floor((math.floor(pygame.time.get_ticks()) - math.floor(start_ticks)) / 10)
    print(seconds)
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
    for i in range(len(allSquares.sprites())):
        allSquares.sprites()[i].updateColor()
    if seconds % 300 == 0 and seconds != 0:
        #moveCurrentBlock()
        print(seconds)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()