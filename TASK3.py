#PROGRAM 3: UGV with Dynamic Obstacles
#Here the obstacles can change position while the UGV is moving.
#The UGV repeatedly calculates a path using A*, moves one step, then checks the environment again.
# PROGRAM 3: UGV NAVIGATION WITH DYNAMIC OBSTACLES

import numpy as np
import matplotlib.pyplot as plt
import heapq
import random
import time

SIZE = 30


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_list:

        _, current = heapq.heappop(open_list)

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()

            return path

        x, y = current

        neighbors = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]

        for nx, ny in neighbors:

            if not (0 <= nx < SIZE and 0 <= ny < SIZE):
                continue

            if grid[nx, ny] == 1:
                continue

            neighbor = (nx, ny)

            new_cost = g_cost[current] + 1

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:

                g_cost[neighbor] = new_cost

                f = new_cost + heuristic(neighbor, goal)

                heapq.heappush(open_list, (f, neighbor))

                came_from[neighbor] = current

    return None


def create_obstacles():

    grid = np.zeros((SIZE, SIZE), dtype=int)

    for _ in range(150):

        x = random.randint(0, SIZE - 1)
        y = random.randint(0, SIZE - 1)

        grid[x, y] = 1

    return grid


def move_dynamic_obstacles(grid, ugv, goal):

    new_grid = np.zeros_like(grid)

    positions = np.argwhere(grid == 1)

    for x, y in positions:

        # Random movement
        directions = [
            (0, 0),
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        dx, dy = random.choice(directions)

        nx = x + dx
        ny = y + dy

        if 0 <= nx < SIZE and 0 <= ny < SIZE:

            if (nx, ny) != ugv and (nx, ny) != goal:
                new_grid[nx, ny] = 1
        else:
            new_grid[x, y] = 1

    return new_grid


# Start and goal
start = (0, 0)
goal = (SIZE - 1, SIZE - 1)

grid = create_obstacles()

grid[start] = 0
grid[goal] = 0

ugv = start
path_history = [ugv]

steps = 0
start_time = time.time()

while ugv != goal and steps < 1000:

    # Re-plan using current obstacle information
    path = astar(grid, ugv, goal)

    if path is None:
        print("UGV could not find a path.")
        break

    # Move one step
    if len(path) > 1:
        ugv = path[1]
        path_history.append(ugv)

    # Obstacles move after UGV moves
    grid = move_dynamic_obstacles(grid, ugv, goal)

    grid[ugv] = 0
    grid[goal] = 0

    steps += 1


execution_time = time.time() - start_time

print("================================")
print("DYNAMIC UGV RESULTS")
print("================================")
print("Start:", start)
print("Goal:", goal)
print("Steps Taken:", steps)
print("Execution Time:", round(execution_time, 4), "seconds")

if ugv == goal:
    print("Mission Status: SUCCESS")
else:
    print("Mission Status: FAILED")


# Plot final environment and UGV path

plt.figure(figsize=(8, 8))

plt.imshow(grid, cmap="gray_r")

x = [p[0] for p in path_history]
y = [p[1] for p in path_history]

plt.plot(y, x, linewidth=2)

plt.scatter(start[1], start[0], s=120, label="Start")
plt.scatter(goal[1], goal[0], s=120, label="Goal")

plt.scatter(ugv[1], ugv[0], s=100, label="UGV")

plt.title("UGV Navigation with Dynamic Obstacles")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

plt.show()