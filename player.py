import os

import pygame

from items import Bullet
from platforms import MovingPlatform

pygame.init()
pygame.mixer.init()

SWORD = pygame.image.load(os.path.join('png', 'sword.png'))
SHIELD = pygame.image.load(os.path.join('png', 'shield.png'))
STAND_R = pygame.image.load(os.path.join('png', 'playerStandR.png'))
WALK_R1 = pygame.image.load(os.path.join('png', 'playerWalkR1.png'))
WALK_R2 = pygame.image.load(os.path.join('png', 'playerWalkR2.png'))
STAND_L = pygame.image.load(os.path.join('png', 'playerStandL.png'))
WALK_L1 = pygame.image.load(os.path.join('png', 'playerWalkL1.png'))
WALK_L2 = pygame.image.load(os.path.join('png', 'playerWalkL2.png'))
FALL_L = pygame.image.load(os.path.join('png', 'playerFallL.png'))
FALL_R = pygame.image.load(os.path.join('png', 'playerFallR.png'))
JUMP_L = pygame.image.load(os.path.join('png', 'playerJumpL.png'))
JUMP_R = pygame.image.load(os.path.join('png', 'playerJumpR.png'))

image_right = [WALK_R1, WALK_R2]
image_left = [WALK_L1, WALK_L2]

HEART = pygame.image.load(os.path.join('png', 'heart.png'))
GOLD = pygame.image.load(os.path.join('png', 'gold.png'))
BULLET_R = pygame.image.load(os.path.join('png', 'bullet_R.png'))
BULLET_L = pygame.image.load(os.path.join('png', 'bullet_L.png'))

shoot_sound = pygame.mixer.Sound(os.path.join('sound', 'shoot.wav'))
gold_sound = pygame.mixer.Sound(os.path.join('sound', 'gold.wav'))
jump_sound = pygame.mixer.Sound(os.path.join('sound', 'jump.wav'))

WHITE = pygame.color.THECOLORS['white']

SCREEN_SIZE = WIDTH, HEIGHT = 960, 660
screen = pygame.display.set_mode(SCREEN_SIZE)


class Player(pygame.sprite.Sprite):
    """
    Klasa obiektu gracza
    """

    def __init__(self, file_image):
        super().__init__()
        self.image = file_image
        self.rect = self.image.get_rect()
        self.items = set()
        self.movement_x = 0
        self.movement_y = 0
        self._count = 0
        self.golds = 0
        self.lives = 5
        self.score = 0
        self.level = None
        self.direction_of_movement = 'right'
        self.protection = False
        self.dead = False
        self.counter = 0

    def turn_right(self):
        if self.direction_of_movement == 'left':
            self.direction_of_movement = 'right'
        self.movement_x = 10

    def turn_left(self):
        if self.direction_of_movement == 'right':
            self.direction_of_movement = 'left'
        self.movement_x = -10

    # metoda odpowiadając za skok
    def jump(self):
        self.rect.y += 2
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)
        self.rect.y -= 2

        if colliding_platforms:
            jump_sound.play()
            self.movement_y = -12

    def run_right(self):
        self.movement_x = 20

    def run_left(self):
        self.movement_x = -20

    def shoot(self):
        if 'gun' in self.items and len(self.level.set_of_bullets) < 2:
            bullet = Bullet(BULLET_R, self.direction_of_movement)
            if self.direction_of_movement == 'left':
                bullet.image = BULLET_L
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.centery = self.rect.centery + 15
            if pygame.sprite.spritecollide(bullet, self.level.set_of_bullets, False):
                bullet.kill()
            else:
                self.level.set_of_bullets.add(bullet)
                shoot_sound.play()

    # metoda prywatna - grawitacja
    def _gravitation(self):
        if self.movement_y == 0:
            self.movement_y = 1
        else:
            self.movement_y += 0.35

    def stop_x(self):
        self.movement_x = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def _move(self, image_list):
        if self._count < 4:
            self.image = image_list[0]
        elif self._count < 8:
            self.image = image_list[1]

        if self._count >= 8:
            self._count = 0
        else:
            self._count += 1

    def update(self):
        self._gravitation()
        # --------------ruch w poziomie---------------
        self.rect.x += self.movement_x

        # sprawdzanie kolizji
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms | self.level.set_of_walls, False)

        for p in colliding_platforms:
            if self.movement_x > 0:
                self.rect.right = p.rect.left
            if self.movement_x < 0:
                self.rect.left = p.rect.right

        # animacje
        if self.movement_x > 0:
            self._move(image_right)
        if self.movement_x < 0:
            self._move(image_left)

        # --------------ruch w poziomie---------------

        # --------------ruch w pionie---------------
        self.rect.y += self.movement_y
        # sprawdzanie kolizji
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms | self.level.set_of_walls, False)
        for p in colliding_platforms:
            if self.movement_y > 0:
                self.rect.bottom = p.rect.top
                if self.direction_of_movement == 'left' and self.movement_x == 0:
                    self.image = STAND_L
                if self.direction_of_movement == 'right' and self.movement_x == 0:
                    self.image = STAND_R
            if self.movement_y < 0:
                self.rect.top = p.rect.bottom

            self.movement_y = 0

            # gracz jedzie razem z platformą
            if isinstance(p, MovingPlatform) and self.movement_x == 0:
                self.rect.x += p.movement_x

        # zmiana grafiki gdy nie jedzie razem z platformą w dół
        self.rect.y += 2
        colliding_platforms = pygame.sprite.spritecollide(
            self, self.level.set_of_platforms, False)
        self.rect.y -= 2

        if not colliding_platforms:
            if self.movement_y > 0:
                if self.direction_of_movement == 'left':
                    self.image = FALL_L
                else:
                    self.image = FALL_R
            if self.movement_y < 0:
                if self.direction_of_movement == 'left':
                    self.image = JUMP_L
                else:
                    self.image = JUMP_R

        # sprawdzamy kolizję z wrogami lub spadek w przepaść
        colliding_enemies = pygame.sprite.spritecollide(
            self, self.level.set_of_enemies, False)

        for enemy in colliding_enemies:
            if self.protection:
                break
            elif enemy.lifes:
                self.lives -= 1
                self.protection = True
                self.counter = 5
                pygame.time.set_timer(pygame.USEREVENT, 500)
                self.rect.center = [480, 330]
        if self.rect.top > HEIGHT:
            self.lives -= 1
            pygame.time.delay(500)
            self.rect.left = 150 + self.level.world_shift
            self.rect.bottom = HEIGHT - 70

            # sprawdzenie kolizji z przedmiotami
        colliding_items = pygame.sprite.spritecollide(
            self, self.level.set_of_items, False)
        for item in colliding_items:
            if item.name == 'gun':
                self.items.add('gun')
                self.score += 100
                item.kill()
            if item.name == 'doors':
                self.items.add('key')
                self.score += 1000
            if item.name == 'sword':
                self.items.add('sword')
                self.score += 2000
                item.kill()
            if item.name == 'shield':
                self.items.add('shield')
                self.score += 5000
                item.kill()
            if item.name == 'jump':
                self.movement_y = -50

        colliding_gold = pygame.sprite.spritecollide(self, self.level.set_of_gold, False)
        for gold in colliding_gold:
            self.golds += 1
            self.score += 200
            gold_sound.play()
            gold.kill()

        # rysowanie żyć na ekranie
        if self.lives:
            for i in range(self.lives):
                screen.blit(HEART, [40 * i + 20, 15])

        if self.items.__contains__('sword'):
            screen.blit(SWORD, [850, 100])

        if self.items.__contains__('shield'):
            screen.blit(SHIELD, [864, 110])

        screen.blit(GOLD, [800, 10])
        font = pygame.font.SysFont("consolas", 30)
        gold_render = font.render(str(self.golds), 1, WHITE)
        screen.blit(gold_render, (920, 30))

        score_render = font.render('wynik: {}'.format(str(self.score)), 1, WHITE)
        screen.blit(score_render, (750, 175))

        if self.protection:
            protection_render = font.render('protection: {} s'.format(str(self.counter)), 1, WHITE)
            screen.blit(protection_render, (780, 250))

    def get_event(self, event):
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.turn_right()
            elif event.key == pygame.K_a:
                self.turn_left()
            elif keys[pygame.K_d] and keys[pygame.K_LSHIFT]:
                self.run_right()
            elif keys[pygame.K_a] and keys[pygame.K_LSHIFT]:
                self.run_left()
            elif event.key == pygame.K_w:
                self.jump()
            if event.key == pygame.K_SPACE:
                self.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d and self.movement_x > 0:
                self.stop_x()
                self.image = STAND_R
            if event.key == pygame.K_a and self.movement_x < 0:
                self.stop_x()
                self.image = STAND_L
            if event.key == pygame.K_LSHIFT and self.movement_x > 0:
                self.turn_right()
            if event.key == pygame.K_d and event.key == pygame.K_LSHIFT and self.movement_x < 0:
                self.turn_right()
            if event.key == pygame.K_LSHIFT and self.movement_x < 0:
                self.turn_left()
            if event.key == pygame.K_a and event.key == pygame.K_LSHIFT and self.movement_x < 0:
                self.turn_left()
