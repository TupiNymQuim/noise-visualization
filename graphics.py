import pygame
import random
from collections import deque

# Screen dimensions
WIDTH = 1200
HEIGHT = 800

# Colors
GREEN = (0, 235, 94)
BLACK = (0, 0, 0)

PACKET_OFFSET = 40
PACKET_SPEED = 10


def add_packets(packets, circles):
    for i, packet_size in enumerate(packets):
        x = (-packet_size) - (i * PACKET_OFFSET)
        # Random vertical position
        y = random.randint(packet_size, HEIGHT - packet_size)
        circles.append([x, y, packet_size])


def animate_packets(circles, screen):
    """
    Animates circles moving left to right, with radius based on number values.

    Args:
        numbers: A list of integers representing the circle radius.
    """

    screen.fill(BLACK)

    out_of_bounds = deque()
    for i, circle in enumerate(circles):
        x, y, radius = circle
        x += PACKET_SPEED
        circles[i][0] = x

        pygame.draw.circle(screen, GREEN, (int(x), int(y)), radius)

        if x > WIDTH + radius:
            out_of_bounds.appendleft(i)

    for i in out_of_bounds:
        del circles[i]

    pygame.display.flip()
