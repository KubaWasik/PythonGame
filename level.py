import os

import pygame

from platforms import MovingPlatform

# grafiki platform
BACKGROUND = pygame.image.load(os.path.join('png', 'background.png'))
dirtLeft = pygame.image.load(os.path.join('png', 'dirtLeft.png'))
dirtMid = pygame.image.load(os.path.join('png', 'dirtMid.png'))
dirtRight = pygame.image.load(os.path.join('png', 'dirtRight.png'))
dirtSingle = pygame.image.load(os.path.join('png', 'dirt.png'))
METAL_L = pygame.image.load(os.path.join('png', 'metal_L.png'))
METAL_C = pygame.image.load(os.path.join('png', 'metal_C.png'))
METAL_R = pygame.image.load(os.path.join('png', 'metal_R.png'))
METAL_SINGLE = pygame.image.load(os.path.join('png', 'metal_single.png'))
wallCenter = pygame.image.load(os.path.join('png', 'wallCenter.png'))
wallRight = pygame.image.load(os.path.join('png', 'wallRight.png'))
wallLeft = pygame.image.load(os.path.join('png', 'wallLeft.png'))
wallTop = pygame.image.load(os.path.join('png', 'wallTop.png'))
wallBottom = pygame.image.load(os.path.join('png', 'wallBottom.png'))
wallTopRight = pygame.image.load(os.path.join('png', 'wallTopRight.png'))
wallTopLeft = pygame.image.load(os.path.join('png', 'wallTopLeft.png'))
wallBottomRight = pygame.image.load(os.path.join('png', 'wallBottomRight.png'))
wallBottomLeft = pygame.image.load(os.path.join('png', 'wallBottomLeft.png'))

dirtList = [dirtSingle, dirtLeft, dirtMid, dirtRight]
METAL_LIST = [METAL_SINGLE, METAL_L, METAL_C, METAL_R]
wallList = [wallCenter, wallLeft, wallTop, wallRight, wallBottom]
wallCornerList = [wallTopLeft, wallTopRight, wallBottomRight, wallBottomLeft]

WIDTH = 960


class Level:
    """
    Klasa bazowa poziomu
    """

    def __init__(self, player=None):
        self.set_of_platforms = set()
        self.set_of_bullets = pygame.sprite.Group()
        self.set_of_items = pygame.sprite.Group()
        self.set_of_gold = pygame.sprite.Group()
        self.set_of_enemies = pygame.sprite.Group()
        self.set_of_enemy_bullets = pygame.sprite.Group()
        self.set_of_moving_enemies = set()
        self.set_of_walls = set()
        self.player = player
        self.world_shift = 0

    def update(self):
        for platform in self.set_of_platforms:
            platform.update()

        self.set_of_gold.update()
        self.set_of_bullets.update()
        self.set_of_enemies.update()
        self.set_of_enemy_bullets.update()

        self._delete_bullets()

        # przesunięcie ekranu gdy gracz jest blisko prawej krawędzi
        if self.player.rect.right >= 450:
            diff = self.player.rect.right - 450
            self.player.rect.right = 450
            self._shift_world(-diff, 0)

        # przesunięcie ekranu gdy gracz jest blisko lewej krawędzi
        if self.player.rect.left <= 450:
            diff = 450 - self.player.rect.left
            self.player.rect.left = 450
            self._shift_world(diff, 0)

        if self.player.rect.top >= 330:
            diff = self.player.rect.top - 330
            self.player.rect.top = 330
            self._shift_world(0, -diff)

        if self.player.rect.bottom <= 330:
            diff = 330 - self.player.rect.bottom
            self.player.rect.bottom = 330
            self._shift_world(0, diff)

    def draw(self, surface):
        surface.blit(BACKGROUND, (0, 0))
        for platform in self.set_of_platforms:
            if isinstance(platform, MovingPlatform):
                platform.draw(surface, METAL_LIST)
            else:
                platform.draw(surface, dirtList)
        self.set_of_bullets.draw(surface)
        self.set_of_items.draw(surface)
        self.set_of_gold.draw(surface)
        self.set_of_enemies.draw(surface)
        self.set_of_enemy_bullets.draw(surface)

        for c in self.set_of_gold:
            c.draw(surface)

        for wall in self.set_of_walls:
            wall.draw(surface, wallList, wallCornerList)

    def _shift_world(self, shift_x, shift_y):
        self.world_shift += shift_x
        self.world_shift += shift_y

        for platform in self.set_of_platforms | self.set_of_walls:
            platform.rect.x += shift_x
            platform.rect.y += shift_y

        for bullet in self.set_of_bullets:
            bullet.rect.x += shift_x
            bullet.rect.y += shift_y

        for item in self.set_of_items:
            item.rect.x += shift_x
            item.rect.y += shift_y

        for gold in self.set_of_gold:
            gold.rect.x += shift_x
            gold.rect.y += shift_y

        for enemy in self.set_of_enemies:
            enemy.rect.x += shift_x
            enemy.rect.y += shift_y

        for enemy_bullet in self.set_of_enemy_bullets:
            enemy_bullet.rect.x += shift_x
            enemy_bullet.rect.y += shift_y

    def _delete_bullets(self):
        pygame.sprite.groupcollide(self.set_of_bullets, self.set_of_enemy_bullets, True, True)
        pygame.sprite.groupcollide(self.set_of_bullets, self.set_of_platforms, True, False)
        pygame.sprite.groupcollide(self.set_of_enemy_bullets, self.set_of_platforms, True, False)
        for bullet in self.set_of_bullets:
            # sprawdzamy kolizję z platformami i usuwamy pociski
            if pygame.sprite.spritecollideany(bullet, self.set_of_platforms | self.set_of_walls):
                bullet.kill()
            # sprawdzamy czy pocisk wyleciał poza planszę i usuwamy go
            if bullet.rect.right > WIDTH or bullet.rect.left < 0:
                bullet.kill()

            # sprawdzamy czy pocisk trafił we wroga i usuwamy obiekty
            colliding_enemies = pygame.sprite.spritecollide(bullet, self.set_of_enemies, False)
            for enemy in colliding_enemies:
                bullet.kill()
                if enemy.lifes:
                    enemy.lifes -= 1
                    self.player.score += 100
                    if not enemy.lifes:
                        enemy.count = 0
