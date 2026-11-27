from heapq import heappop, heappush
from .maze import Maze, Position


def manhattan_distance(a: Position, b: Position) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def best_first_search(maze: Maze, start: Position, goal: Position) -> list[Position]:
    path, _ = best_first_search_with_stats(maze, start, goal)
    return path

def best_first_search_with_stats(maze: Maze, start: Position, goal: Position) -> tuple[list[Position], int]:
    if not maze.is_walkable(start) or not maze.is_walkable(goal):
        return [], 0

    frontier: list[tuple[int, int, Position]] = []
    came_from: dict[Position, Position | None] = {start: None}
    heappush(frontier, (manhattan_distance(start, goal), 0, start))
    expanded = 0

    while frontier:
        _, _, current = heappop(frontier)
        expanded += 1

        if current == goal:
            break

        for neighbor in maze.neighbors(current):
            if neighbor in came_from:
                continue
            order = len(came_from)
            came_from[neighbor] = current
            heappush(frontier, (manhattan_distance(neighbor, goal), order, neighbor))
    else:
        return [], expanded

    path: list[Position] = []
    current: Position | None = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    return list(reversed(path)), expanded
