import pygame

from enemy import Enemy


class Platform(pygame.sprite.Sprite):
    """
    Klasa zwykłej platformy
    """

    def __init__(self, width, height, rect_x, rect_y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y

    def draw(self, surface, image_list):
        if self.width == 70:
            surface.blit(image_list[0], self.rect)
        else:
            surface.blit(image_list[1], self.rect)
            for i in range(70, self.width - 70, 70):
                surface.blit(image_list[2], [self.rect.x + i, self.rect.y])
            surface.blit(image_list[3], [self.rect.x + self.width - 70, self.rect.y])


# ruchoma platforma
class MovingPlatform(Platform):
    """
    Klasa ruchomej platformy
    """

    def __init__(self, width, height, rect_x, rect_y):
        super().__init__(width, height, rect_x, rect_y)
        self.movement_x = 0
        self.movement_y = 0
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
        self.level = None

    def update(self):
        # ruch prawo/lewo
        self.rect.x += self.movement_x
        # sprawdzamy kontakt z graczem
        colliding_sprites = pygame.sprite.spritecollide(
            self, self.level.set_of_moving_enemies | {self.level.player}, False)
        for sp in colliding_sprites:
            if self.movement_x < 0:
                sp.rect.right = self.rect.left
            else:
                sp.rect.left = self.rect.right

        # ruch góra/dół
        self.rect.y += self.movement_y
        # sprawdzamy kontakt z graczem i ruchomymi
        colliding_sprites = pygame.sprite.spritecollide(
            self, self.level.set_of_moving_enemies | {self.level.player}, False)

        for sp in colliding_sprites:
            if self.movement_y < 0:
                sp.rect.bottom = self.rect.top
            else:
                sp.rect.top = self.rect.bottom

        # sprawdzamy granice i decydujemy o zmianie kierunku
        if self.rect.bottom > self.boundary_bottom \
                or self.rect.top < self.boundary_top:
            self.movement_y *= -1

        position = self.rect.x - self.level.world_shift
        if position < self.boundary_left or position + self.rect.width > self.boundary_right:
            self.movement_x *= -1


class PlatformEnemy(Enemy):
    """
    Klasa platformy z przeciwnikami
    """

    def update(self):
        super().update()
        if self.rect.left < self.platform.rect.left or \
                self.rect.right > self.platform.rect.right:
            self.movement_x *= -1

        if self.movement_x > 0 and self.direction_of_movement == 'left':
            self.direction_of_movement = 'right'

        if self.movement_x < 0 and self.direction_of_movement == 'right':
            self.direction_of_movement = 'left'
