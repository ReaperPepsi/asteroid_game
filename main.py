import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y, PLAYER_RADIUS)



    while(True):
        dt = clock.tick(60) / 1000
        screen.fill((0,0,0)) #color the window with black


        # loop used to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        


if __name__ == "__main__":
    main()
