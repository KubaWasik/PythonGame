import os
import random

import pygame

pygame.init()
pygame.mixer.init()

alienStandR = pygame.image.load(os.path.join('png', 'alienStandR.png'))
alienWalkR1 = pygame.image.load(os.path.join('png', 'alienWalkR1.png'))
alienWalkR2 = pygame.image.load(os.path.join('png', 'alienWalkR2.png'))
alienWalkL1 = pygame.image.load(os.path.join('png', 'alienWalkL1.png'))
alienWalkL2 = pygame.image.load(os.path.join('png', 'alienWalkL2.png'))
alienDeadR = pygame.image.load(os.path.join('png', 'alienDeadR.png'))
alienDeadL = pygame.image.load(os.path.join('png', 'alienDeadL.png'))

alienWalkR = [alienWalkR1, alienWalkR2]
alienWalkL = [alienWalkL1, alienWalkL2]
alienDeadR = [alienDeadR, alienDeadR]
alienDeadL = [alienDeadL, alienDeadL]

death_sound = pygame.mixer.Sound(os.path.join('sound', 'death.wav'))

BULLET_R = pygame.image.load(os.path.join('png', 'bullet_R.png'))
BULLET_L = pygame.image.load(os.path.join('png', 'bullet_L.png'))


class Enemy(pygame.sprite.Sprite):
    """
    Klasa wroga (kosmity)
    """

    def __init__(self, start_image, image_right, image_left, image_dead_right,
                 image_dead_left, platform=None, movement_x=0, movement_y=0):
        super().__init__()
        self.image = start_image
        self.rect = self.image.get_rect()
        self.movement_x = movement_x
        self.movement_y = movement_y
        self.direction_of_movement = 'right'
        self.platform = platform
        self.image_right = image_right
        self.image_left = image_left
        self.image_dead_right = image_dead_right
        self.image_dead_left = image_dead_left
        self.lives = 2
        self.count = 0

        if self.platform:
            self.rect.bottom = self.platform.rect.top
            self.rect.centerx = random.randint(
                self.platform.rect.left + self.rect.width,
                self.platform.rect.right - self.rect.width)

    def update(self):
        if not self.lives and self.count > 7:
            death_sound.play()
            self.kill()

        self.rect.x += self.movement_x
        self.rect.y += self.movement_y

        # animacje
        if self.lives:
            if self.movement_x > 0:
                self._move(self.image_right)
            if self.movement_x < 0:
                self._move(self.image_left)
        else:
            if self.direction_of_movement == 'right':
                self._move(self.image_dead_right)
            else:
                self._move(self.image_dead_left)

        if not random.randint(1, 100) % 33:
            self.image = self.image_left

    def _move(self, image_list):
        if self.count < 4:
            self.image = image_list[0]
        elif self.count < 8:
            self.image = image_list[1]

        if self.count >= 8:
            self.count = 0
        else:
            self.count += 1
