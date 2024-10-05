Here is the solution:
```java
public int maxFill(List<List<Integer>> grid, int capacity) {
    int rows = grid.size();
    int cols = grid.get(0).size();
    int[][] water = new int[rows][cols];
    int[][] visited = new int[rows][cols];
    int res = 0;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid.get(i).get(j) == 1) {
                water[i][j] = 1;
            }
        }
    }

    while (true) {
        boolean changed = false;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (water[i][j] == 1 && visited[i][j] == 0) {
                    changed = true;
                    int cnt = 0;
                    for (int k = 0; k < rows; k++) {
                        for (int m = 0; m < cols; m++) {
                            if (water[k][m] == 1 && Math.abs(k - i) + Math.abs(m - j) <= capacity) {
                                water[k][m] = 0;
                                cnt++;
                            }
                        }
                    }
                    if (cnt > 0) {
                        visited[i][j] = 1;
                        res += cnt;
                    }
                }
            }
        }
        if (!changed) {
            break;
        }
    }
    return res;
}
```
The idea is to use a BFS to mark the wells that can be emptied by the bucket. For each well, we check all its neighbors that are within the bucket capacity. If a neighbor is within the capacity, we mark it as emptied and increment the count of wells emptied. We repeat this process until no more wells can be emptied. The total number of times we need to lower the bucket is the sum of the counts of wells emptied in each iteration.