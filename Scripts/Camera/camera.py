import math
import pygame
from Scripts.Player.player import Player
from Scripts.sprite import PNGSprite


class Camera(pygame.sprite.Group):

    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]
        self.half_hight = self.display_surface.get_size()[1]
        self.ground_surf = pygame.image.load('Sprites/Ground.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft=(0, 0))
        self.offset = pygame.Vector2(0, 0)



    def center_player(self, player: Player):
        self.offset[0] = player.position.x - self.half_width
        self.offset[1] = player.position.y - self.half_hight

    def sorted_draw(self):

        # Ground
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf, ground_offset)

        # Env Player and Enemys
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.bottom):
            if isinstance(sprite, PNGSprite):
                self.display_surface.blit(sprite.image, sprite.rect)
            else:
                sprite_offset = sprite.rect.topleft + self.offset
                self.display_surface.blit(sprite.image, sprite_offset)

