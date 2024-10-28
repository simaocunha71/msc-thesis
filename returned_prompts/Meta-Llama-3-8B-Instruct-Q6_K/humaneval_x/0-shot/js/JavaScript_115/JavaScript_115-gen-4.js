Here is a Python solution that uses a queue to simulate the process of emptying the wells. It starts by initializing a queue with all the wells that are not empty. Then, it enters a loop that continues until the queue is empty. In each iteration of the loop, it extracts a well from the queue, fills the bucket with water from the well, and then returns the well to the queue. The loop continues until all the wells are empty.

```Python
from collections import deque

def maxFill(grid, capacity):
    m, n = len(grid), len(grid[0])
    queue = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                queue.append((i, j))
    ans = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if grid[x][y] == 1:
                grid[x][y] = 0
                if x > 0 and grid[x-1][y] == 1:
                    queue.append((x-1, y))
                if x < m-1 and grid[x+1][y] == 1:
                    queue.append((x+1, y))
                if y > 0 and grid[x][y-1] == 1:
                    queue.append((x, y-1))
                if y < n-1 and grid[x][y+1] == 1:
                    queue.append((x, y+1))
                ans += 1
    return ans
```

This solution has a time complexity of O(m*n) and a space complexity of O(m*n), where m is the number of rows and n is the number of columns in the grid. It uses a queue to store the wells that need to be emptied, and it iterates over the queue until all the wells are empty. The solution fills the bucket with water from the well, and then returns the well to the queue. The loop continues until all the wells are empty.

Note that the solution assumes that the bucket capacity is 1, as specified in the problem statement. If the bucket capacity is different, the solution would need to be modified accordingly. For example, if the bucket capacity is 2, the solution would need to fill the bucket with 2 units of water from each well, and then return the well to the queue.