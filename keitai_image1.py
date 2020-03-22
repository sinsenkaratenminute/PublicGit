import sys
import pygame
from pygame.locals import QUIT,Rect,KEYDOWN,K_LEFT,K_RIGHT

pygame.init()
pygame.key.set_repeat(900,900)
#画面の大きさ
SURFACE = pygame.display.set_mode((1200,800))
FPSCLOCK = pygame.time.Clock()

def main():
    strip = pygame.image.load("strip100.png")
    images = []
    for index in range(9):
        image = pygame.Surface((100,100))
        image.blit(strip,(0,0),Rect(index * 100,0,100,100))
        images.append(image)

    counter = 0
    pos_x = 400
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pos_x -= 100
                elif event.key == K_RIGHT:
                    pos_x += 100

        # 画面の色
        SURFACE.fill((0,0,0))

        SURFACE.blit(images[counter % 2 + 0],(200,200))
        SURFACE.blit(images[counter % 2 + 2],(400,200))
        SURFACE.blit(images[counter % 2 + 4],(600,200))
        SURFACE.blit(images[counter % 2 + 6],(800,200))
        counter += 1

        SURFACE.blit(images[8],(pos_x,600))

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()