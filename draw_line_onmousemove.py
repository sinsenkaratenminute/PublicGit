import sys
import pygame
from pygame.locals import QUIT,MOUSEBUTTONDOWN,MOUSEMOTION,MOUSEBUTTONUP

pygame.init()
pygame.key.set_repeat(5,5)
#画面の大きさ
SURFACE = pygame.display.set_mode((300,200))
FPSCLOCK = pygame.time.Clock()

def main():
    mousepos = []
    mousedown = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousedown = True
            elif event.type == MOUSEMOTION:
                if mousedown:
                    mousepos.append(event.pos)
            elif event.type == MOUSEBUTTONUP:
                mousedown = False
            #     mousepos .clear()

        # 画面の色
        SURFACE.fill((255, 255, 255))
        if len(mousepos) > 1:
            pygame.draw.lines(SURFACE,(255,0,0),False,mousepos)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()