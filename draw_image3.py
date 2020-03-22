#画像を開店すると軸がぶれてしまう

import sys
import pygame
from pygame.locals import QUIT,Rect

pygame.init()
#画面の大きさ
SURFACE = pygame.display.set_mode((900,900))
FPSCLOCK = pygame.time.Clock()

def main():
    logo = pygame.image.load("pythonlogo.png")
    theta= 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        theta += 1
        # 画面の色
        SURFACE.fill((255, 255, 255))

        #ロゴを回転し、左上が（100,30）の位置にロゴを描画
        new_logo = pygame.transform.rotate(logo,theta)
        SURFACE.blit(new_logo,(100,30))

        pygame.display.update()
        FPSCLOCK.tick(50)

if __name__ == '__main__':
    main()