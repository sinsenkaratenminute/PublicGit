import sys
import pygame
from pygame.locals import QUIT,Rect

pygame.init()
#画面の大きさ
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load("pylogo.jpg")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 画面の色
        SURFACE.fill((255, 255, 255))
        SURFACE.blit(logo,(0,0))
        SURFACE.blit(logo,(255,50),Rect(50,50,100,100))

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()