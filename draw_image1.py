import sys
import pygame
from pygame.locals import QUIT,Rect

pygame.init()
#画面の大きさ
SURFACE = pygame.display.set_mode((900,900))
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load("pythonlogo.png")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 画面の色
        SURFACE.fill((255, 255, 255))

        #左下が（100,100）の位置にロゴを描写
        SURFACE.blit(logo,(100,100))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()