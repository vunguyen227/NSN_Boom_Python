import pygame
from pygame import mixer

# Initialize the pygame
pygame.init()

# mixer.music.load('./data/sounds/background.wav')
# mixer.music.play(-1)

WIDTH, HEIGHT = 1300, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NSN Boooooom")
BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load("./data/images/background1.jpg"), (850, 850))
FPS = 60
GAME_AREA = pygame.Rect(25, 25, 850, 850)

objects = {}
BombsList = []
BombExplored = []
