import pygame
from random import *

GRAY = (150,150,150)
LIGHTBLUE = (120, 167, 255)

BLOCKS = ["I", "J", "L", "O", "Z", "S", "T"]

IBlock = [0, 3],[1, 3], [2, 3], [3, 3]

currentBlock = []

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

#print(spaces)

#print(len(spaces))

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

  def updateColor(self):
    if len(currentBlock[0]) > 0:
      for i in range(len(currentBlock[0])):
        spaces[currentBlock[0][i][0]][currentBlock[0][i][1]] = 1
    if spaces[self.index[0]][self.index[1]] != 0:
      if spaces[self.index[0]][self.index[1]] == 1:
        self.image.fill(LIGHTBLUE)

def createNewBlock():
  blockChoice = choice(BLOCKS)
  blockChoice = "I"
  if blockChoice == "I":
    currentBlock.append(IBlock)

def moveCurrentBlock():
  for i in range(4):
    currentBlock[0][i][0] += 1
    print("loop " + str(i) + ": " + str(currentBlock[0][i]))
    if currentBlock[0][i][0] > 8:
      removeCurrentBlock()
  print("-------")

def removeCurrentBlock():
  currentBlock.clear()
  print("Current Block: " + currentBlock)

createNewBlock()
print(len(currentBlock[0]))
print(currentBlock[0][0])

