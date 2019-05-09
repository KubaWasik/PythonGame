import os

import pygame

from level_one import LevelOne
from level_two import LevelTwo
from player import Player

# inicjacja PyGame
pygame.init()

# stałe
STAND_R = pygame.image.load(os.path.join('png', 'playerStandR.png'))

# kolory
DARK_RED = pygame.color.THECOLORS['darkred']
LIGHT_BLUE = pygame.color.THECOLORS['lightblue']
LIGHT_RED = pygame.color.THECOLORS['palevioletred']
ORANGE_RED = pygame.color.THECOLORS['orangered']
OLIVE = pygame.color.THECOLORS['olivedrab']
DARK_GREEN = pygame.color.THECOLORS['darkgreen']
LIGHT_GREEN = pygame.color.THECOLORS['lightgreen']

# pozycja myszy
mouse = pygame.mouse.get_pos()

# wyśrodkowanie
os.environ['SDL_VIDEO_CENTERED'] = '1'

# ustawienia ekranu i gry
SCREEN_SIZE = WIDTH, HEIGHT = 960, 660
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Prosta gra PyGame')
clock = pygame.time.Clock()


class Text:
    """
    Klasa tekst, odpowiedzialna za rysowanie tekstu na ekranie
    """

    def __init__(self, text, text_color, size=74):
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, size)
        self.image = self.font.render(str(self.text), 1, self.text_color)
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Button:
    """
    Klasa przycisku w oknie gry
    """

    def __init__(self, text, width, height, x, y, background_colour, text_colour):
        self.text = text
        self.width = width
        self.height = height
        self.background_colour = background_colour
        self.text_colour = text_colour
        self.font = pygame.font.SysFont(None, 72)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = [x, y]
        self.image = self.font.render(self.text, 1, self.text_colour, self.background_colour)
        self.rect_image = self.image.get_rect()
        self.rect_image.center = self.rect.center

    def draw(self, surface):
        surface.fill(self.background_colour, self.rect)
        surface.blit(self.image, self.rect_image)


def start():
    is_start = True
    pause_text = Text('Witaj w grze', DARK_RED)
    pause_text.rect.center = WIDTH // 2, HEIGHT // 2
    pause_text.draw(screen)
    cont = Button("Nowa gra", 200, 75, (WIDTH // 4), (HEIGHT // 4) * 3, LIGHT_GREEN, DARK_GREEN)
    cont.draw(screen)
    ext = Button("Wyjdź", 200, 75, (WIDTH // 4) * 3, (HEIGHT // 4) * 3, LIGHT_RED, DARK_RED)
    ext.draw(screen)

    while is_start:
        for start_event in pygame.event.get():
            if start_event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif start_event.type == pygame.KEYDOWN:
                if start_event.key == pygame.K_ESCAPE:
                    is_start = False
            elif start_event.type == pygame.MOUSEBUTTONDOWN:
                if cont.rect.collidepoint(*pygame.mouse.get_pos()):
                    is_start = False
                    pygame.time.delay(500)
                elif ext.rect.collidepoint(*pygame.mouse.get_pos()):
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(30)


def pause():
    is_pause = True
    pause_text = Text('PAUZA', DARK_RED)
    pause_text.rect.center = WIDTH // 2, HEIGHT // 2
    pause_text.draw(screen)
    cont = Button("Kontynuuj", 200, 75, (WIDTH // 4), (HEIGHT // 4) * 3, LIGHT_GREEN, DARK_GREEN)
    cont.draw(screen)
    ext = Button("Wyjdź", 200, 75, (WIDTH // 4) * 3, (HEIGHT // 4) * 3, LIGHT_RED, DARK_RED)
    ext.draw(screen)

    while is_pause:
        for pause_event in pygame.event.get():
            if pause_event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif pause_event.type == pygame.KEYDOWN:
                if pause_event.key == pygame.K_ESCAPE:
                    is_pause = False
            elif pause_event.type == pygame.MOUSEBUTTONDOWN:
                if cont.rect.collidepoint(*pygame.mouse.get_pos()):
                    is_pause = False
                    pygame.time.delay(500)
                elif ext.rect.collidepoint(*pygame.mouse.get_pos()):
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(30)


def win():
    is_win = True
    header = Text('WYGRAŁEŚ!!!', DARK_RED)
    header.rect.center = WIDTH // 2, HEIGHT // 4
    header.draw(screen)
    main_text = Text('Zdobiłeś wielki miecz absolutu i tarczę wielkiego myśliciela', DARK_RED, 50)
    main_text.rect.center = WIDTH // 2, HEIGHT // 2
    main_text.draw(screen)
    cont = Button("Zobacz wyniki", 200, 75, (WIDTH // 4), (HEIGHT // 4) * 3, LIGHT_GREEN, DARK_GREEN)
    cont.draw(screen)
    ext = Button("Wyjdź", 200, 75, (WIDTH // 4) * 3, (HEIGHT // 4) * 3, LIGHT_RED, DARK_RED)
    ext.draw(screen)

    while is_win:
        for win_event in pygame.event.get():
            if win_event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif win_event.type == pygame.KEYDOWN:
                if win_event.key == pygame.K_ESCAPE:
                    is_win = False
            elif win_event.type == pygame.MOUSEBUTTONDOWN:
                if cont.rect.collidepoint(*pygame.mouse.get_pos()):
                    is_win = False
                    pygame.time.delay(500)
                elif ext.rect.collidepoint(*pygame.mouse.get_pos()):
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(30)


def not_win():
    is_not_win = True
    header = Text('NIESTETY NIE WYGRAŁEŚ', DARK_RED)
    header.rect.center = WIDTH // 2, HEIGHT // 4
    header.draw(screen)
    main_text_1 = Text('Nie znalazłeś miecza absolutu', DARK_RED, 50)
    main_text_1.rect.center = WIDTH // 2, HEIGHT // 2 - 100
    main_text_1.draw(screen)
    main_text_2 = Text('ani tarczy wielkiego myśliciela', DARK_RED, 50)
    main_text_2.rect.center = WIDTH // 2, HEIGHT // 2
    main_text_2.draw(screen)
    cont = Button("Zobacz wyniki", 200, 75, (WIDTH // 4), (HEIGHT // 4) * 3, ORANGE_RED, OLIVE)
    cont.draw(screen)
    ext = Button("Wyjdź", 200, 75, (WIDTH // 4) * 3, (HEIGHT // 4) * 3, LIGHT_RED, DARK_RED)
    ext.draw(screen)

    while is_not_win:
        for not_win_event in pygame.event.get():
            if not_win_event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif not_win_event.type == pygame.KEYDOWN:
                if not_win_event.key == pygame.K_ESCAPE:
                    is_not_win = False
            elif not_win_event.type == pygame.MOUSEBUTTONDOWN:
                if cont.rect.collidepoint(*pygame.mouse.get_pos()):
                    is_not_win = False
                    pygame.time.delay(500)
                elif ext.rect.collidepoint(*pygame.mouse.get_pos()):
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(30)


def end_game():
    screen.fill(LIGHT_BLUE)
    is_not_win = True
    header = Text('KONIEC', DARK_RED)
    header.rect.center = WIDTH // 2, HEIGHT // 4
    header.draw(screen)
    main_text = Text('Zdobyłeś {} punktów!'.format(player.score), DARK_RED, 50)
    main_text.rect.center = WIDTH // 2, HEIGHT // 2 - 100
    main_text.draw(screen)
    ext = Button("Wyjdź", 200, 75, (WIDTH // 4) * 3, (HEIGHT // 4) * 3, LIGHT_RED, DARK_RED)
    ext.draw(screen)

    while is_not_win:
        for not_win_event in pygame.event.get():
            if not_win_event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif not_win_event.type == pygame.KEYDOWN:
                if not_win_event.key == pygame.K_ESCAPE:
                    is_not_win = False
            elif not_win_event.type == pygame.MOUSEBUTTONDOWN:
                if ext.rect.collidepoint(*pygame.mouse.get_pos()):
                    pygame.quit()
                    quit()

        pygame.display.update()
        clock.tick(30)


# konkretyzacja obiektów
player = Player(STAND_R)
current_level = LevelOne(player)
level = 1
player.level = current_level
player.rect.center = screen.get_rect().center
finish_text = Text('KONIEC GRY', DARK_RED)

pygame.mixer.music.load(os.path.join('sound', 'soundtrack.mp3'))
pygame.mixer.music.play(-1, 0.0)

gameIcon = pygame.image.load(os.path.join('png', 'icon.png'))
pygame.display.set_icon(gameIcon)
screen.fill(LIGHT_BLUE)
start()

# główna pętla gry
window_open = True
while window_open:
    mouse = pygame.mouse.get_pos()
    screen.fill(LIGHT_BLUE)
    # pętla zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
            elif event.key == pygame.K_p:
                pause()
            elif event.key == pygame.K_h:
                if player.golds > 2 and player.lives < 5:
                    player.lives += 1
                    player.golds -= 3
                    player.score -= 500
        elif event.type == pygame.QUIT:
            window_open = False
        if event.type == pygame.USEREVENT:
            player.counter -= 1
            if player.counter > 0:
                continue
            else:
                player.protection = False
        if 'key' in player.items:
            if level == 1:
                level += 1
                current_level = LevelTwo(player)
                player.level = current_level
                player.items.remove('key')
                if player.items.__contains__('gun'):
                    player.items.remove('gun')
            elif level == 2:
                if player.items.__contains__('sword') and player.items.__contains__('shield'):
                    win()
                    end_game()
                    window_open = False
                else:
                    not_win()
                    end_game()
                    window_open = False

        player.get_event(event)

    if not player.lives:
        player.dead = True
        end_game()
        window_open = False

    # rysowanie i aktualizacja obiektów
    current_level.draw(screen)
    player.update()
    player.draw(screen)
    current_level.update()

    # aktualizacja okna pygame
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
