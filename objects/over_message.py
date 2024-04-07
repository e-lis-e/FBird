import pygame
import configs
import assets
from layer import Layer


class OverMessage(pygame.sprite.Sprite):
     def __init__(self, *groups):

        self._layer = Layer.UI

        self.image = assets.get_sprite("gameover")
        self.rect = self.image.get_rect(center=(configs.screen_width / 2, configs.screen_height / 2))
        
        super().__init__(*groups)