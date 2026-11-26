import math
import sys
from .maze import Maze, Position

def mnhtn_d(a: Position, b:Position) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bfs(maze: Maze, start: Position, goal: Position) -> list[Position]:
    if not maze.is_walkable(start) or not maze.is_walkable(goal):
        return[]
    if start == goal:
        return [start]
    