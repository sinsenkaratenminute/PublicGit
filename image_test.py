import sys
from math import sin,cos,radians
import pygame
from pygame.locals import QUIT,Rect

pygame.init()
#画面の大きさ
SURFACE = pygame.display.set_mode((900,900))
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load("invater.jpg")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 画面の色
        SURFACE.fill((255, 255, 255))

        # 緑
        pygame.draw.ellipse(SURFACE, (0, 255, 0), (50, 150, 110, 60), 5)
        pygame.draw.ellipse(SURFACE, (0, 255, 0), ((250, 130), (90, 90)), 20)

        pointlist0,pointlist1 = [],[]
        for theta in range(0,360,72):
            rad = radians(theta)
            pointlist0.append((cos(rad)*100 + 100,sin(rad)*100 + 150))
            pointlist1.append((cos(rad)*100 + 300,sin(rad)*100 + 150))

        pygame.draw.lines(SURFACE,(0,255,0),True,pointlist0)
        pygame.draw.polygon(SURFACE,(255,0,0),pointlist1)

        #左下が（100,100）の位置にロゴを描写
        SURFACE.blit(logo, (10, 10))
        # SURFACE.blit(logo,(500,500))
        # SURFACE.blit(logo, (700, 500))
        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()