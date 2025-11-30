import numpy as np

maze = np.array([
    [2,1,1,1,1,1,1,0,1,0],
    [1,0,1,0,0,0,1,0,1,1],
    [1,1,0,0,1,1,1,0,1,0],
    [1,0,0,0,0,0,0,0,1,0],
    [1,1,1,1,1,1,1,1,1,0],
    [0,1,0,0,1,0,0,0,0,0],
    [1,1,0,0,1,0,0,0,1,1],
    [1,0,1,1,1,0,0,1,1,0],
    [1,0,1,0,0,0,0,0,1,0],
    [1,0,1,1,1,1,1,1,1,3]
])

def find_neighbors(pos, maze):
    x, y = pos
    steps = [(-1,0), (1,0), (0,-1), (0,1)]
    result = []
    for dx, dy in steps:
        nx, ny = x + dx, y + dy
        if 0 <= nx < maze.shape[0] and 0 <= ny < maze.shape[1]:
            if maze[nx, ny] != 0: 
                result.append((nx, ny))
    return result

def dfs(maze):
    start = tuple(np.argwhere(maze == 2)[0])
    visited = set()

    def explore(pos):
        if pos in visited:
            return False
        visited.add(pos)

        x, y = pos
        print("Currently at:", pos)

        if maze[x, y] == 3:
            print("FOUND GOAL at:", pos)
            return True

        for neighbor in find_neighbors(pos, maze):
            if explore(neighbor):
                return True
        
        return False
    
    explore(start)

dfs(maze)