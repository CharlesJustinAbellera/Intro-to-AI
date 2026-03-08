# Example 2: Game Character Finding a Treasure

import heapq

# Map of locations and path costs
map_graph = {
    "Village": {"Forest": 2, "River": 5},
    "Forest": {"Cave": 4, "Hill": 2},
    "River": {"Hill": 3},
    "Hill": {"Treasure": 4},
    "Cave": {"Treasure": 1},
    "Treasure": {}
}

# Heuristic values (estimated distance to treasure)
heuristic = {
    "Village": 7,
    "Forest": 4,
    "River": 5,
    "Hill": 2,
    "Cave": 1,
    "Treasure": 0
}

def a_star(start, goal):
    open_list = [(0, start)]
    g_score = {start: 0}
    parent = {}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in map_graph[current].items():
            new_cost = g_score[current] + cost

            if neighbor not in g_score or new_cost < g_score[neighbor]:
                g_score[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                parent[neighbor] = current

path = a_star("Village", "Treasure")

print("Best path to treasure:", path)