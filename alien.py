import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс создающей одного пришельца"""

    def __init__(self, ai_game):
        """Инициализируем пришельца и задаем начальное положение"""
        super(Alien, self).__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загружаем изображение пришельца
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохраняем точной горизонтальной позиции
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """ Возвращает True если пришелец находится у края"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
