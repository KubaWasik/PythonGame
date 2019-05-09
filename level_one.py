import os
import random

import pygame

from items import Gold, Item
from level import Level
from platforms import MovingPlatform, Platform, PlatformEnemy
from wall import Wall

DARK_RED = pygame.color.THECOLORS['darkred']
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

GUN = pygame.image.load(os.path.join('png', 'gun.png'))
GOLD = pygame.image.load(os.path.join('png', 'gold.png'))
DOORS = pygame.image.load(os.path.join('png', 'doors.png'))
SWORD = pygame.image.load(os.path.join('png', 'sword.png'))


class LevelOne(Level):
    """
    Klasa pierwszego poziomu gry
    """

    def __init__(self, player=None):
        super().__init__(player)
        ws_platform_static = [[6 * 70, 70, 6 * 70, 6 * 70], [9 * 70, 70, 0, -3 * 70], [2 * 70, 70, 0, 8 * 70],
                              [2 * 70, 70, 12 * 70, 12 * 70], [4 * 70, 70, 14 * 70, 9 * 70], [70, 70, 13 * 70, 6 * 70],
                              [70, 70, 17 * 70, 4 * 70], [70, 70, 13 * 70, 3 * 70], [7 * 70, 70, 12 * 70, -1 * 70],
                              [70, 70, 28 * 70, 10 * 70], [6 * 70, 70, 32 * 70, 11 * 70], [70, 70, 30 * 70, 7 * 70],
                              [70, 70, 33 * 70, 6 * 70], [70, 70, 36 * 70, 5 * 70], [70, 70, 19 * 70, 7 * 70],
                              [6 * 70, 70, 26 * 70, 2 * 70], [2 * 70, 70, 34 * 70, 0], [70, 70, 15 * 70, -2 * 70]]
        # tworzymy platformy
        for el in ws_platform_static:
            platform_object = Platform(*el)
            self.set_of_platforms.add(platform_object)

        # rozmieszczanie monet
        self.gold_table = [[13 * 70 + 25, 20], [14 * 70 + 45, 20], [15 * 70 + 55, 20], [17 * 70 + 15, 20],
                           [19 * 70 + 10, 5 * 70 + 45],
                           [36 * 70 + 55, -6 * 70 - 35], [13 * 70 + 45, -2 * 70 - 45], [35, -70 - 35], [70, -70 - 35],
                           [70 + 35, -70 - 35],
                           [2 * 70, -70 - 35], [2 * 70 + 35, -70 - 35], [3 * 70, -70 - 35], [3 * 70 + 35, -70 - 35],
                           [4 * 70, -70 - 35]]

        for g_table in self.gold_table:
            gold = Gold(*g_table)
            gold.image = GOLD
            self.set_of_gold.add(gold)

        sword = Item(SWORD, 'sword')
        sword.rect.x = 19 * 70
        sword.rect.y = -2 * 70
        self.set_of_items.add(sword)

        ws_walls = [[70, 22 * 70, -70, -7 * 70], [40 * 70, 70, -70, -8 * 70], [70, 22 * 70, 38 * 70, -7 * 70],
                    [70, 7 * 70, 12 * 70, 0],
                    [70, 5 * 70, 6 * 70, 7 * 70], [70, 2 * 70, 12 * 70, 13 * 70], [70, 12 * 70, 18 * 70, -2 * 70],
                    [70, 4 * 70, 12 * 70, -5 * 70]]

        # tworzymy ściany
        for el in ws_walls:
            wall_objects = Wall(*el)
            self.set_of_walls.add(wall_objects)

        # tworzymy ruchomą platformę (ruch w poziomie)
        mp_x = MovingPlatform(210, 40, 20 * 70, 2 * 70)
        mp_x.boundary_left = 20 * 70
        mp_x.boundary_right = 23 * 70
        mp_x.movement_x = 2
        mp_x.player = self.player
        mp_x.level = self
        self.set_of_platforms.add(mp_x)

        # tworzymy przedmiot (broń)
        gun = Item(GUN, 'gun')
        gun.rect.x = 50
        gun.rect.bottom = 7 * 70 + 45
        self.set_of_items.add(gun)

        doors = Item(DOORS, 'doors')
        doors.rect.x = 0
        doors.rect.bottom = -3 * 70
        self.set_of_items.add(doors)

        # tworzymy wrogów z platformami
        ws_enemy_platform1 = [[12 * 70, 70, 0, 14 * 70]]  # 36*70, 70, 0, 14*70
        for el in ws_enemy_platform1:
            platform_object = Platform(*el)
            self.set_of_platforms.add(platform_object)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)

        ws_enemy_platform2 = [[25 * 70, 70, 13 * 70, 14 * 70]]
        for el in ws_enemy_platform2:
            platform_object = Platform(*el)
            self.set_of_platforms.add(platform_object)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)

        ws_enemy_platform3 = [[5 * 70, 70, 22 * 70, 9 * 70]]
        for el in ws_enemy_platform3:
            platform_object = Platform(*el)
            self.set_of_platforms.add(platform_object)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)

        ws_enemy_platform4 = [[15 * 70, 70, 18 * 70, -3 * 70]]
        for el in ws_enemy_platform4:
            platform_object = Platform(*el)
            self.set_of_platforms.add(platform_object)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)

        ws_enemy_platform5 = [[12 * 70, 70, 0, 0]]
        for el in ws_enemy_platform5:
            platform_object = Platform(*el)
            self.set_of_platforms.add(platform_object)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)
            platform_enemy = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                           alienDeadR, alienDeadL, platform_object,
                                           random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy)
