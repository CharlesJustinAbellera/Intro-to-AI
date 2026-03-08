#Example 1: Finding the Shortest Route Between Cities

import heapq

# Graph representing cities and distances
graph = {
    "Start": {"A": 4, "B": 2},
    "A": {"C": 3, "D": 2},
    "B": {"A": 1, "D": 4},
    "C": {"Goal": 2},
    "D": {"Goal": 3},
    "Goal": {}
}

# Heuristic estimate to goal
heuristic = {
    "Start": 7,
    "A": 5,
    "B": 6,
    "C": 2,
    "D": 1,
    "Goal": 0
}

def a_star(start, goal):
    open_list = [(0, start)]
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
            return path[::-1]

        for neighbor, cost in graph[current].items():
            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

print("Best route:", a_star("Start", "Goal"))