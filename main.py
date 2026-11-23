import cairo
import pygame
import sys


MAP = [
    "###########",
    "#...#.....#",
    "#.#.#.###.#",
    "#.#...#...#",
    "#.#####.#.#",
    "#.........#",
    "###########",
]

maze = [list(row) for row in MAP]  # # = tembok, . = lantai
ROWS = len(maze)
COLS = len(maze[0])