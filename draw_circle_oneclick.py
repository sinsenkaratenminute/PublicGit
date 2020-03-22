import sys
import pygame
from pygame.locals import QUIT,MOUSEBUTTONDOWN

pygame.init()
#画面の大きさ
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    mouthpos = []

    while True:
        # 画面の色
        SURFACE.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouthpos.append(event.pos)

        for i,j in mouthpos:
            pygame.draw.circle(SURFACE,(255,0,0),(i,j),5)

        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()


