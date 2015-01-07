__author__ = 'Adrian'

import pygame
import os.path
import math
from pygame.locals import *

# Globals
WIDTH = 1024
HEIGHT = 768

main_dir = os.path.split(os.path.abspath(__file__))[0]

# helper functions


def load_image(file):
    """loads an image, prepares it for play"""
    file = os.path.join(main_dir, 'art', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    return surface.convert_alpha()


def load_sound(file):
    file = os.path.join(main_dir, 'audio', file)
    sound = pygame.mixer.Sound(file)
    return sound


def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def process_sprite_group(group, screen):
    for elem in set(group):
        elem.draw(screen)
        is_old = elem.update()
        if is_old:
            group.remove(elem)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Space Arena')

    # Load the background
    background = load_image('background.png')

    clock = pygame.time.Clock()
    # Game loop
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()