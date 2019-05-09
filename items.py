import pygame


class Item(pygame.sprite.Sprite):
    """
    Klasa bazowa przedmiotu
    """

    def __init__(self, image, name):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.name = name


class Bullet(pygame.sprite.Sprite):
    """
    Klasa pocisku
    """

    def __init__(self, image, direction):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.direction_of_movement = direction

    def update(self):
        if self.direction_of_movement == 'right':
            self.rect.x += 30
        else:
            self.rect.x -= 30


class Gold(pygame.sprite.Sprite):
    def __init__(self, rect_x, rect_y):
        super().__init__()
        self.image = pygame.surface.Surface([80, 80])
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface):
        surface.blit(self.image, self.rect)
