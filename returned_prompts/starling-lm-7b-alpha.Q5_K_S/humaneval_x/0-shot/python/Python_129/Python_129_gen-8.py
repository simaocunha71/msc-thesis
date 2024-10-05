
# Time:  O(N^2 + k)
# Space: O(N^2)

class Solution(object):
    def minPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        min_heap = []
        lookup = {}
        for r in xrange(len(grid)):
            for c in xrange(len(grid[r])):
                lookup[grid[r][c]] = (r, c)
        min_heap.append((1, (grid[0][0],)))
        while min_heap:
            curr, path = heapq.heappop(min_heap)
            if len(path) == k:
                return path
            for d in directions:
                nr, nc = r+d[0], c+d[1]
                if not (0 <= nr < len(grid) and
                        0 <= nc < len(grid[nr]) and
                        (nr, nc) not in path and
                        grid[nr][nc] not in lookup):
                    continue
                new_path = path + (grid[nr][nc],)
                if len(new_path) >= k:
                    if new_path[-1] < new_path[-k]:
                        continue
                heapq.heappush(min_heap, (curr+1, new_path))
        return []


```
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```