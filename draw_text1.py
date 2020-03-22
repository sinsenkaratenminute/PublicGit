import sys
import pygame
from pygame.locals import QUIT,Rect

pygame.init()
#画面の大きさ
SURFACE = pygame.display.set_mode((800,600))
FPSCLOCK = pygame.time.Clock()

def main():
    sysfont = pygame.font.SysFont(None,50)
    message = sysfont.render("Hello!Nice to Meet You!",True,(0,120,120))
    message_rect = message.get_rect()
    message_rect.center = (200,100)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 画面の色
        SURFACE.fill((255, 255, 255))
        SURFACE.blit(message,message_rect)
        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()