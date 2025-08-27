import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT /2) 
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for obj in asteroids:
            if(obj.collision(player)):
                print("Game over!")
                return
        screen.fill((0,0,0))
        
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    

if __name__ == "__main__":
    main()
