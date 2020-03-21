import sys
import pygame
from pygame.locals import QUIT,Rect

pygame.init()
SURFACE = pygame.display.set_mode((400,250))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            SURFACE.fill((255,255,255))

            #赤：横線
            pygame.draw.line(SURFACE,(255,0,0),(10,80),(200,80))

            #赤：横線（太さ１５）
            pygame.draw.line(SURFACE, (255, 0, 0), (10,150),(200,150),15)

            #緑：縦線
            pygame.draw.line(SURFACE,(0,255,0),(250,30),(250,200))

            #青：車線（太さ10）
            start_pos = (300,30)
            end_pos = (280,200)

            pygame.draw.line(SURFACE,(0,0,255),start_pos,end_pos,10)

            pygame.display.update()
            FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()