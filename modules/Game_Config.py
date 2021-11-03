import pygame
from pygame import mixer

# Initialize the pygame
pygame.init()

# Audio
mixer.music.load('./data/sounds/background.wav')
mixer.music.play(-1)

FONT = pygame.font.Font('./data/font/prstart.ttf',15)

S = 50  # pixel per square

WIDTH, HEIGHT = S*26, S*18

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NSN Boooooom")
BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load("./data/images/background1.jpg"), (S*17, S*17))
PANEL_IMAGE = pygame.transform.scale(
    pygame.image.load("./data/images/backright.png"), (S*8, S*18))
FPS = 60
GAME_AREA = pygame.Rect(S/2, S/2, S*17, S*17)
CLOCK = pygame.time.Clock()


BitMap = []
ObjsList = {}
BombsList = {}
ExploringBomb = []
ItemsList = {}


def coordInGame(pos):
    return (pos[1]*S+S/2, pos[0]*S+S/2)
