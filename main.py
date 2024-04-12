import os
import random
import math
import pygame
import asyncio
from os import listdir
from os.path import isfile, join

pygame.init()  # start pygame

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name,))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("tile14.png")

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Good Bye")
                running = False
                break

        draw(window, background, bg_image)

    pygame.quit()
    quit()


# async def main():
#     pass


# Run the game
main(screen)
