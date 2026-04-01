import pygame
from constants import *
from logger import log_state
import player
import asteroid
import asteroidfield
import shot
from logger import log_event
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    shot.Shot.containers = (shots, drawable, updatable)
    asteroidfield.AsteroidField.containers = (updatable,)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    player.Player.containers = (updatable, drawable)
    asteroid_field = asteroidfield.AsteroidField()
    player_instance = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for rock in asteroids:
            if rock.collides_with(player_instance) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if rock.collides_with(bullet):
                    log_event("asteroid_shot")
                    rock.split()
                    bullet.kill()
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
