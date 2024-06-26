import pygame
from scripts.functions import load_image
class Sprite:
      def __init__(self, image, coords ):
            self.image = image
            self.rect = image.get_frect()
            self.rect.center = coords
      
      def render(self, scene , offset_y):
            rect = self.rect.move(0, - offset_y)
            scene.blit(self.image,rect)

      def collide(self, other_rect):
            self.rect.colliderect(other_rect)
            
