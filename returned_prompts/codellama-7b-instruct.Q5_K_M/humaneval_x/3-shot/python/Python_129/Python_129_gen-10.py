    # Time: O(N*N*log(N*N))
    # Space: O(N*N)
    # Dijkstra's algorithm
    # The key idea is to treat the grid as a graph where the distance between the cells are the absolute difference
    # between their values.
    # Then find the k shortest paths from the starting node to the ending node.
    # We can use the heapq module to implement a priority queue
    # The priority is the distance from the starting node, and the value of the cell in the path.
    # We will put the distance to the starting node as 0.
    # When we find the shortest path, we will put the distance to the ending node as the priority
    # We will keep track of the cells we visit and put the cell in the ending node as the priority.
    # We will stop when we find the shortest path with the ending node as the cell with the lowest priority.

    N = len(grid)
    M = len(grid[0])

    if k > N * M:
        return []

    start_node = (0, 0)
    end_node = (N - 1, M - 1)
    distance = 0
    heap = [(0, start_node, [start_node])]
    visited = set()

    while len(heap) > 0:
        dist, node, path = heapq.heappop(heap)
        if node == end_node:
            distance = dist
            break
        visited.add(node)
        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                heapq.heappush(heap, (dist + abs(grid[neighbor[0]][neighbor[1]] - grid[node[0]][node[1]]), neighbor, path + [neighbor]))

    return [grid[node[0]][node[1]] for node in path]


def get_neighbors(node, grid):
    N = len(grid)
    M = len(grid[0])
    neighbors = []
    if node[0] > 0:
        neighb