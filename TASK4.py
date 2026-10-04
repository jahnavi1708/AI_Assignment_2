#PROGRAM 4: Indian Route Search
#This replaces the classic Arad → Bucharest Romania problem with an Indian-city route problem
#We'll use A* because it combines path cost and heuristic information.

# PROGRAM 4: INDIAN CITY ROUTE USING A*

import heapq

# Indian city road network
graph = {
    "Delhi": {
        "Jaipur": 280,
        "Agra": 230,
        "Lucknow": 550
    },

    "Jaipur": {
        "Delhi": 280,
        "Ahmedabad": 670,
        "Agra": 240
    },

    "Agra": {
        "Delhi": 230,
        "Jaipur": 240,
        "Lucknow": 330
    },

    "Lucknow": {
        "Delhi": 550,
        "Agra": 330,
        "Patna": 530
    },

    "Ahmedabad": {
        "Jaipur": 670,
        "Mumbai": 530
    },

    "Mumbai": {
        "Ahmedabad": 530,
        "Pune": 150
    },

    "Pune": {
        "Mumbai": 150,
        "Hyderabad": 560
    },

    "Hyderabad": {
        "Pune": 560,
        "Bengaluru": 570,
        "Vijayawada": 275
    },

    "Bengaluru": {
        "Hyderabad": 570,
        "Chennai": 350
    },

    "Chennai": {
        "Bengaluru": 350,
        "Vijayawada": 450
    },

    "Vijayawada": {
        "Hyderabad": 275,
        "Chennai": 450,
        "Visakhapatnam": 350
    },

    "Visakhapatnam": {
        "Vijayawada": 350
    },

    "Patna": {
        "Lucknow": 530
    }
}


# Simple heuristic estimates to Hyderabad
heuristic = {
    "Delhi": 1550,
    "Jaipur": 1250,
    "Agra": 1250,
    "Lucknow": 1100,
    "Ahmedabad": 1200,
    "Mumbai": 710,
    "Pune": 560,
    "Hyderabad": 0,
    "Bengaluru": 570,
    "Chennai": 630,
    "Vijayawada": 275,
    "Visakhapatnam": 600,
    "Patna": 1500
}


def a_star(start, goal):

    open_list = []

    heapq.heappush(
        open_list,
        (heuristic[start], 0, start)
    )

    came_from = {}

    g_cost = {
        city: float("inf")
        for city in graph
    }

    g_cost[start] = 0

    while open_list:

        f, current_cost, current = heapq.heappop(open_list)

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)

            return path[::-1], g_cost[goal]

        for neighbor, distance in graph[current].items():

            new_cost = g_cost[current] + distance

            if new_cost < g_cost[neighbor]:

                g_cost[neighbor] = new_cost
                came_from[neighbor] = current

                f_cost = new_cost + heuristic[neighbor]

                heapq.heappush(
                    open_list,
                    (f_cost, new_cost, neighbor)
                )

    return None, float("inf")


print("Available Cities:")
print(", ".join(graph.keys()))

start = input("\nEnter starting city: ")
goal = input("Enter destination city: ")

if start not in graph or goal not in graph:

    print("Invalid city.")

else:

    path, distance = a_star(start, goal)

    if path is None:

        print("No route found.")

    else:

        print("\nOptimal/Best Route:")
        print(" -> ".join(path))

        print("\nTotal Road Distance:",
              distance, "km")