#PROGRAM 1: Dijkstra's Algorithm for Indian Cities
#This implements Dijkstra on an Indian-city road network and lets you enter a start and destination city.

# PROGRAM 1: DIJKSTRA'S ALGORITHM FOR INDIAN CITIES

import heapq

# Indian city road network
# Distances are approximate road distances in km
graph = {
    "Delhi": {
        "Jaipur": 280,
        "Lucknow": 550,
        "Chandigarh": 245,
        "Agra": 230
    },
    "Jaipur": {
        "Delhi": 280,
        "Ahmedabad": 670,
        "Agra": 240,
        "Udaipur": 395
    },
    "Ahmedabad": {
        "Jaipur": 670,
        "Mumbai": 530,
        "Surat": 265,
        "Udaipur": 260
    },
    "Mumbai": {
        "Ahmedabad": 530,
        "Pune": 150,
        "Nashik": 170,
        "Goa": 590
    },
    "Pune": {
        "Mumbai": 150,
        "Hyderabad": 560,
        "Bengaluru": 840
    },
    "Hyderabad": {
        "Pune": 560,
        "Bengaluru": 570,
        "Chennai": 630,
        "Nagpur": 500,
        "Vijayawada": 275
    },
    "Bengaluru": {
        "Pune": 840,
        "Hyderabad": 570,
        "Chennai": 350,
        "Mysuru": 145
    },
    "Chennai": {
        "Bengaluru": 350,
        "Hyderabad": 630,
        "Vijayawada": 450
    },
    "Vijayawada": {
        "Hyderabad": 275,
        "Chennai": 450,
        "Visakhapatnam": 350
    },
    "Visakhapatnam": {
        "Vijayawada": 350,
        "Bhubaneswar": 440
    },
    "Bhubaneswar": {
        "Visakhapatnam": 440,
        "Kolkata": 440
    },
    "Kolkata": {
        "Bhubaneswar": 440,
        "Patna": 585
    },
    "Patna": {
        "Kolkata": 585,
        "Lucknow": 530
    },
    "Lucknow": {
        "Delhi": 550,
        "Patna": 530,
        "Agra": 330
    },
    "Agra": {
        "Delhi": 230,
        "Jaipur": 240,
        "Lucknow": 330
    },
    "Chandigarh": {
        "Delhi": 245
    },
    "Udaipur": {
        "Jaipur": 395,
        "Ahmedabad": 260
    },
    "Surat": {
        "Ahmedabad": 265,
        "Mumbai": 285
    },
    "Nashik": {
        "Mumbai": 170
    },
    "Goa": {
        "Mumbai": 590
    },
    "Nagpur": {
        "Hyderabad": 500
    },
    "Mysuru": {
        "Bengaluru": 145
    }
}


def dijkstra(graph, start, goal):
    distances = {city: float('inf') for city in graph}
    previous = {city: None for city in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        if current_distance > distances[current_city]:
            continue

        if current_city == goal:
            break

        for neighbor, distance in graph[current_city].items():
            new_distance = current_distance + distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_city
                heapq.heappush(priority_queue, (new_distance, neighbor))

    # Construct path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if distances[goal] == float('inf'):
        return None, float('inf')

    return path, distances[goal]


print("Available cities:")
print(", ".join(graph.keys()))

start = input("\nEnter starting city: ")
goal = input("Enter destination city: ")

if start not in graph or goal not in graph:
    print("Invalid city name.")
else:
    path, distance = dijkstra(graph, start, goal)

    if path is None:
        print("No route found.")
    else:
        print("\nShortest Route:")
        print(" -> ".join(path))
        print("\nTotal Distance:", distance, "km")