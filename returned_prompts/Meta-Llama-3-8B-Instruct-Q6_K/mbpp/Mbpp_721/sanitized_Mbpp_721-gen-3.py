from typing import List
def maxAverageOfPath(matrix: List[List[int]]) -> float:
    n = len(matrix)
    directions = [(0, 1), (1, 0)]
    max_avg = float('-inf')
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            total_cost = 0
            visited = set((i, j))
            queue = [(i, j, 0)]
            while queue:
                x, y, cost = queue.pop(0)
                total_cost += matrix[x][y]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                        queue.append((nx, ny, cost + matrix[nx][ny]))
                        visited.add((nx, ny))
            avg = total_cost / len(visited)
            max_avg = max(max_avg, avg)
    return max_avg