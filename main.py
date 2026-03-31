import pygame
import constants
from logger import log_state
import player
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT

def main():
    pygame.init()
    Player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        Player.update(dt)
        screen.fill("black")
        Player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
