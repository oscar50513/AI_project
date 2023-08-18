import pygame
import pygame.event
import sys


def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))
def getKey(keyName):
    s = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    mykey = pygame.key.get_pressed()
    keyName = getattr(pygame, "K_{}".format(keyName))
    if mykey[keyName]:
        s = True
    pygame.display.update()
    return s

if __name__ == "__main__":
    init()
