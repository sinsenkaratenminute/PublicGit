import sys
import random
import pygame
from pygame.locals import QUIT,Rect

pygame.init()
#画面の大きさ
SURFACE = pygame.display.set_mode((1200,600))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #画面の色
        SURFACE.fill((0,0,0))

        pointlist = []
        for _ in range(10):
            xpos = random.randint(0,1200)
            ypos = random.randint(0,600)
            pointlist.append((xpos,ypos))

        pygame.draw.lines(SURFACE,(255,255,255),True,pointlist,5)

        pygame.display.update()
        FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()