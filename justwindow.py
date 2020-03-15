#! /usr/bin/env/python3
import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((700,300))
pygame.display.set_caption("窓の大きさ")

def main():
    """main routine"""
    while True:
        SURFACE.fill((0,0,255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()
