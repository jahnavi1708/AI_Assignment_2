#PROGRAM 2: UGV with Static Obstacles
#This creates a 70 × 70 grid, generates obstacles at three different densities, and uses A* to find the shortest path.
#It also shows the path visually and calculates simple Measures of Effectiveness.

# PROGRAM 2: UGV NAVIGATION WITH STATIC OBSTACLES

import numpy as np
import matplotlib.pyplot as plt
import heapq
import random
import time

SIZE = 70

# Three obstacle density levels
DENSITIES = {
    "Low": 0.15,
    "Medium": 0.30,
    "High": 0.45
}


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

            if nx < 0 or nx >= SIZE or ny < 0 or ny >= SIZE:
                continue

            if grid[nx, ny] == 1:
                continue

            new_cost = g_cost[current] + 1

            neighbor = (nx, ny)

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:

                g_cost[neighbor] = new_cost

                f = new_cost + heuristic(neighbor, goal)

                heapq.heappush(open_list, (f, neighbor))

                came_from[neighbor] = current

    return None


def generate_grid(density):

    grid = np.random.choice(
        [0, 1],
        size=(SIZE, SIZE),
        p=[1 - density, density]
    )

    # Keep start and goal free
    grid[0, 0] = 0
    grid[SIZE - 1, SIZE - 1] = 0

    return grid


def run_experiment(name, density):

    grid = generate_grid(density)

    start = (0, 0)
    goal = (SIZE - 1, SIZE - 1)

    start_time = time.time()

    path = astar(grid, start, goal)

    execution_time = time.time() - start_time

    obstacle_count = np.sum(grid == 1)

    print("\n-----------------------------")
    print("Density:", name)
    print("Obstacle Percentage:", density * 100, "%")
    print("Number of Obstacles:", obstacle_count)
    print("Execution Time:", round(execution_time, 6), "seconds")

    if path:

        path_length = len(path) - 1

        print("Path Found: YES")
        print("Path Length:", path_length)

        # Simple MOE
        success = 1
        efficiency = path_length / (SIZE * 2 - 2)

        print("Mission Success:", success)
        print("Path Efficiency:", round(efficiency, 3))

        # Plot
        plt.figure(figsize=(7, 7))

        plt.imshow(grid, cmap="gray_r")

        path_x = [p[0] for p in path]
        path_y = [p[1] for p in path]

        plt.plot(path_y, path_x, linewidth=2)

        plt.scatter(0, 0, s=100, label="Start")
        plt.scatter(SIZE - 1, SIZE - 1, s=100, label="Goal")

        plt.title("UGV Path - " + name + " Obstacle Density")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.show()

    else:

        print("Path Found: NO")
        print("Mission Success: 0")


# Run all three densities

for name, density in DENSITIES.items():
    run_experiment(name, density)