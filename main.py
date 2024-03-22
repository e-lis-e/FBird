import pygame
import assets
import configs

from objects.bg import Bg

pygame.init()

screen = pygame.display.set_mode((configs.screen_width, configs.screen_height))
clock = pygame.time.Clock()
running = True

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

Bg(0, sprites)
Bg(1, sprites)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    sprites.draw(screen)
    sprites.update()

    pygame.display.flip()
    clock.tick(configs.fps)


pygame.quit()