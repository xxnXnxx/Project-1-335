# Ian Gabriel Vista
# Algorithm
def detect_loop(coordinates):
    n = len(coordinates)
    visited = set()

    for i in range(n):
        if i not in visited:
            if dfs(coordinates, i, visited):
                return "Loop detected"

    return "No loop detected"

def dfs(coordinates, current, visited):
    visited.add(current)

    # Get the current coordinate
    x, y = coordinates[current]

    # Assuming neighbors are directly connected coordinates
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    for i, neighbor in enumerate(coordinates):
        if neighbor in neighbors and i not in visited:
            if dfs(coordinates, i, visited):
                return True

    return False

# Sample input
coordinates = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 2), (4, 6)]

result = detect_loop(coordinates)
print(result)
