import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    game_end = True
    while game_end:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(("Black"))
        #updatable = pygame.sprite.Group()
        #drawable = pygame.sprite.Group()
        #Player.constainers = (drawable, updatable)
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)
        #player.draw(screen)
        #player.update(dt)
        pygame.display.flip()
        ticking = clock.tick(60)
        dt = ticking / 1000


if __name__ == "__main__":
    main()
