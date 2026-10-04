#PROGRAM 5: Telangana District Map Coloring
#This implements the map-coloring problem for Telangana districts using Backtracking/CSP.

# PROGRAM 5: MAP COLORING OF TELANGANA DISTRICTS

import matplotlib.pyplot as plt

# Telangana district adjacency graph
# Each district is connected to its neighboring districts.

graph = {

    "Adilabad": {
        "Nirmal",
        "Komaram Bheem Asifabad",
        "Mancherial"
    },

    "Komaram Bheem Asifabad": {
        "Adilabad",
        "Mancherial"
    },

    "Mancherial": {
        "Adilabad",
        "Komaram Bheem Asifabad",
        "Peddapalli",
        "Jagtial"
    },

    "Nirmal": {
        "Adilabad",
        "Nizamabad",
        "Kamareddy",
        "Jagtial"
    },

    "Nizamabad": {
        "Nirmal",
        "Kamareddy",
        "Jagtial"
    },

    "Kamareddy": {
        "Nizamabad",
        "Nirmal",
        "Siddipet",
        "Rajanna Sircilla"
    },

    "Jagtial": {
        "Nirmal",
        "Nizamabad",
        "Mancherial",
        "Peddapalli",
        "Rajanna Sircilla"
    },

    "Peddapalli": {
        "Mancherial",
        "Jagtial",
        "Jayashankar Bhupalpally",
        "Karimnagar"
    },

    "Rajanna Sircilla": {
        "Jagtial",
        "Kamareddy",
        "Karimnagar",
        "Siddipet"
    },

    "Karimnagar": {
        "Peddapalli",
        "Rajanna Sircilla",
        "Siddipet",
        "Hanamkonda"
    },

    "Siddipet": {
        "Kamareddy",
        "Rajanna Sircilla",
        "Karimnagar",
        "Hanamkonda",
        "Jangaon",
        "Yadadri Bhuvanagiri"
    },

    "Jayashankar Bhupalpally": {
        "Peddapalli",
        "Mulugu",
        "Warangal",
        "Mahabubabad"
    },

    "Mulugu": {
        "Jayashankar Bhupalpally",
        "Warangal",
        "Bhadradri Kothagudem"
    },

    "Warangal": {
        "Jayashankar Bhupalpally",
        "Mulugu",
        "Hanamkonda",
        "Mahabubabad"
    },

    "Hanamkonda": {
        "Warangal",
        "Karimnagar",
        "Siddipet",
        "Jangaon"
    },

    "Jangaon": {
        "Siddipet",
        "Hanamkonda",
        "Yadadri Bhuvanagiri",
        "Suryapet"
    },

    "Yadadri Bhuvanagiri": {
        "Siddipet",
        "Jangaon",
        "Nalgonda",
        "Suryapet",
        "Medchal-Malkajgiri"
    },

    "Nalgonda": {
        "Yadadri Bhuvanagiri",
        "Suryapet",
        "Nagarkurnool"
    },

    "Suryapet": {
        "Jangaon",
        "Yadadri Bhuvanagiri",
        "Nalgonda",
        "Khammam"
    },

    "Khammam": {
        "Suryapet",
        "Bhadradri Kothagudem",
        "Mahabubabad"
    },

    "Bhadradri Kothagudem": {
        "Khammam",
        "Mulugu",
        "Mahabubabad"
    },

    "Mahabubabad": {
        "Warangal",
        "Jayashankar Bhupalpally",
        "Khammam",
        "Bhadradri Kothagudem"
    },

    "Nagarkurnool": {
        "Nalgonda",
        "Wanaparthy",
        "Mahabubnagar",
        "Nagar Kurnool"
    },

    "Mahabubnagar": {
        "Nagarkurnool",
        "Wanaparthy",
        "Narayanpet"
    },

    "Wanaparthy": {
        "Nagarkurnool",
        "Mahabubnagar",
        "Jogulamba Gadwal"
    },

    "Jogulamba Gadwal": {
        "Wanaparthy",
        "Narayanpet"
    },

    "Narayanpet": {
        "Mahabubnagar",
        "Jogulamba Gadwal",
        "Vikarabad"
    },

    "Vikarabad": {
        "Narayanpet",
        "Sangareddy",
        "Rangareddy"
    },

    "Sangareddy": {
        "Vikarabad",
        "Medak",
        "Kamareddy",
        "Rangareddy"
    },

    "Medak": {
        "Sangareddy",
        "Kamareddy",
        "Siddipet"
    },

    "Rangareddy": {
        "Vikarabad",
        "Sangareddy",
        "Medchal-Malkajgiri",
        "Hyderabad"
    },

    "Medchal-Malkajgiri": {
        "Rangareddy",
        "Yadadri Bhuvanagiri",
        "Hyderabad"
    },

    "Hyderabad": {
        "Rangareddy",
        "Medchal-Malkajgiri"
    }
}


# Remove duplicate/special naming issue
if "Nagar Kurnool" in graph:
    graph["Nagarkurnool"].discard("Nagar Kurnool")


# Available colors
colors = ["Red", "Green", "Blue", "Yellow"]


def is_safe(district, color, assignment):

    for neighbor in graph[district]:

        if neighbor in assignment and assignment[neighbor] == color:
            return False

    return True


def map_coloring(assignment):

    if len(assignment) == len(graph):
        return True

    # Select uncolored district
    uncolored = [
        district
        for district in graph
        if district not in assignment
    ]

    # Choose district with most neighbors first
    district = max(
        uncolored,
        key=lambda x: len(graph[x])
    )

    for color in colors:

        if is_safe(district, color, assignment):

            assignment[district] = color

            if map_coloring(assignment):
                return True

            del assignment[district]

    return False


assignment = {}

if map_coloring(assignment):

    print("TELANGANA MAP COLORING")
    print("======================")

    for district, color in sorted(assignment.items()):
        print(f"{district:30} : {color}")

else:

    print("No valid coloring found.")


# Verify solution

valid = True

for district in graph:

    for neighbor in graph[district]:

        if neighbor in assignment:

            if assignment[district] == assignment[neighbor]:
                valid = False

print("\nSolution Valid:", valid)

print("\nNumber of Colors Used:",
      len(set(assignment.values())))

print("Colors Used:",
      set(assignment.values()))