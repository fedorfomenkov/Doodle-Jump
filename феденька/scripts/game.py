import os
import pygame
from scripts.functions import load_image
from scripts.sprite import Sprite
from scripts.player import Player
from scripts.constants import display_size


class Game:
      def __init__(self):
            self.background = load_image('assets' , 'images' , 'background.png')
            self.platforms = [
                  Sprite(load_image('assets', 'images', 'platform.png'), (240, 700)),
                  Sprite(load_image('assets', 'images', 'platform.png'), (100, 450)),
                  Sprite(load_image('assets', 'images', 'platform.png'), (380, 250)),
            ]
            
            self.player = Player(
                  load_image('assets', 'images', 'player.png'),
                  (240, 600),
                  4,
                  20,
                  0.75,
            )
            self.offset_y = 0
      
      def render_objects(self, scene):
            scene.blit(self.background, (0, 0))
            for platform in self.platforms:
                  platform.render(scene, self.offset_y)
            self.player.render(scene, self.offset_y)

      def process_key_down_event(self, key):
            if key == pygame.K_a:
                  self.player.is_walking_left = True
            if key == pygame.K_d:
                  self.player.is_walking_right = True
            

      def process_key_up_event(self, key):
            if key == pygame.K_a:
                  self.player.is_walking_left = False
            if key == pygame.K_d:
                  self.player.is_walking_right = False
      
      def render_object(self, scene):
            scene.blit(self.background_image, (0, 0))
            for platform in self.platforms:
                  platform.render(scene)
            self.player.render(scene)
      def update_objects(self):
            for platform in self.platforms:
                  if self.player.collide(platform.rect):
                        self.player.on_platform = True
            self.player.update()
            self.offset_y = self.player.rect.bottom - display_size[1] / 3

      


