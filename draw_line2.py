import sys
import pygame
from pygame.locals import QUIT,Rect

pygame.init()
#画面の大きさ
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #画面の色
            SURFACE.fill((0,0,0))

            for ypos in range(0,400,25):
                pygame.draw.line(SURFACE,0xFFFFFF,(ypos,0),(ypos,300))

            for ypos in range(0,300,25):
                pygame.draw.line(SURFACE,0xFFFFFF,(0,ypos),(400,ypos))

            pygame.display.update()
            FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()