"""
from collections import deque
def maxAverageOfPath(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_avg = -1
    for i in range(rows):
        for j in range(cols):
            dq = deque([(i, j)])
            cost = 0
            visited = set()
            while dq:
                x, y = dq.popleft()
                visited.add((x, y))
                cost += matrix[x][y]
                if x == rows-1 and y == cols-1:
                    max_avg = max(max_avg, cost/len(visited))
                    break
                for nx, ny in [(x+1, y), (x, y+1)]:
                    if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                        dq.append((nx, ny))
    return max_avg
"""
