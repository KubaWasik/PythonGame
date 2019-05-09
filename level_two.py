import os
import random

import pygame

from items import Gold, Item
from level import Level
from platforms import Platform, PlatformEnemy
from wall import Wall

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
SHIELD = pygame.image.load(os.path.join('png', 'shield.png'))
JUMP = pygame.image.load(os.path.join('png', 'jump.png'))


class LevelTwo(Level):
    """
    Klasa drugiego poziomu gry
    """

    def __init__(self, player=None):
        super().__init__(player)
        ws_platform_static = [[4 * 70, 70, 0, -10 * 70], [4 * 70, 70, 16 * 70, -10 * 70],
                              [4 * 70, 70, 0, -4 * 70], [4 * 70, 70, 16 * 70, -4 * 70],
                              [4 * 70, 70, 0, 2 * 70], [4 * 70, 70, 16 * 70, 2 * 70], [6 * 70, 70, 7 * 70, 5 * 70],
                              [4 * 70, 70, 0, 8 * 70], [4 * 70, 70, 16 * 70, 8 * 70]]

        # tworzymy platformy
        for el in ws_platform_static:
            platform_objects = Platform(*el)
            self.set_of_platforms.add(platform_objects)

        ws_walls = [[70, 20 * 70, -70, -9 * 70], [70, 20 * 70, 20 * 70, -9 * 70], [70, 7 * 70, 0, 29 * 70]]

        # tworzymy ściany
        for el in ws_walls:
            wall_objects = Wall(*el)
            self.set_of_walls.add(wall_objects)

        # rozmieszczanie przedmiotów specjalnych
        self.gold_table = [[9 * 70, 4 * 70], [10 * 70 + 35, 4 * 70], [12 * 70, 4 * 70], [70, -11 * 70],
                           [2 * 70 + 35, -11 * 70],
                           [17 * 70, -11 * 70], [18 * 70 + 35, -11 * 70], [70, -11 * 70], [2 * 70 + 35, -11 * 70],
                           [17 * 70, -5 * 70], [18 * 70 + 35, -5 * 70], [70, -5 * 70], [2 * 70 + 35, -5 * 70],
                           [17 * 70, 70], [18 * 70 + 35, 70], [70, 70], [2 * 70 + 35, 70],
                           [17 * 70, 7 * 70], [18 * 70 + 35, 7 * 70], [70, 7 * 70], [2 * 70 + 35, 7 * 70]]

        for g_table in self.gold_table:
            gold = Gold(*g_table)
            gold.image = GOLD
            self.set_of_gold.add(gold)

        gun = Item(GUN, 'gun')
        gun.rect.x = 800
        gun.rect.bottom = 550
        self.set_of_items.add(gun)

        jump = Item(JUMP, 'jump')
        jump.rect.x = 19 * 70
        jump.rect.bottom = 33 * 70
        self.set_of_items.add(jump)

        doors = Item(DOORS, 'doors')
        doors.rect.x = 0
        doors.rect.bottom = -4 * 70
        self.set_of_items.add(doors)

        shield = Item(SHIELD, 'shield')
        shield.rect.x = 2 * 70
        shield.rect.y = 34 * 70
        self.set_of_items.add(shield)

        # tworzymy wrogów z platformami
        ws_enemy_platform1 = [[16 * 70, 70, 0, 14 * 70]]
        for el in ws_enemy_platform1:
            platform_objects = Platform(*el)
            self.set_of_platforms.add(platform_objects)
            platform_enemy1 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy1)
            platform_enemy2 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy2)
            platform_enemy3 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy3)

        ws_enemy_platform2 = [[15 * 70, 70, 70, 29 * 70]]
        for el in ws_enemy_platform2:
            platform_objects = Platform(*el)
            self.set_of_platforms.add(platform_objects)
            platform_enemy1 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy1)
            platform_enemy2 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy2)
            platform_enemy3 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy3)
            platform_enemy4 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy4)
            platform_enemy5 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy5)
            platform_enemy6 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy6)

        ws_enemy_platform3 = [[20 * 70, 70, 70, 35 * 70]]
        for el in ws_enemy_platform3:
            platform_objects = Platform(*el)
            self.set_of_platforms.add(platform_objects)
            platform_enemy1 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy1)
            platform_enemy2 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy2)
            platform_enemy3 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy3)
            platform_enemy4 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy4)
            platform_enemy5 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy5)

        ws_enemy_platform4 = [[6 * 70, 70, 7 * 70, -7 * 70]]
        for el in ws_enemy_platform4:
            platform_objects = Platform(*el)
            self.set_of_platforms.add(platform_objects)
            platform_enemy1 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy1)
            platform_enemy2 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy2)

        ws_enemy_platform5 = [[6 * 70, 70, 7 * 70, -70]]
        for el in ws_enemy_platform5:
            platform_objects = Platform(*el)
            self.set_of_platforms.add(platform_objects)
            platform_enemy1 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy1)
            platform_enemy2 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy2)

        ws_enemy_platform6 = [[6 * 70, 70, 7 * 70, 11 * 70]]
        for el in ws_enemy_platform6:
            platform_objects = Platform(*el)
            self.set_of_platforms.add(platform_objects)
            platform_enemy1 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy1)
            platform_enemy2 = PlatformEnemy(alienStandR, alienWalkR, alienWalkL,
                                            alienDeadR, alienDeadL, platform_objects,
                                            random.choice([-3, -2, -1, 1, 2, 3]))
            self.set_of_enemies.add(platform_enemy2)
