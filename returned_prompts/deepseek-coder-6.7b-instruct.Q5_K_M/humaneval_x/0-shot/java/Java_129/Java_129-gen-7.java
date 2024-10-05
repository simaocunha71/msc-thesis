        int n = grid.size();
        int[][] dist = new int[n * n + 1][k + 1];
        for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
        dist[1][0] = 0;

B:
        for (int steps = 0; steps <= k; ++steps)
            for (int cell = 1; cell <= n * n; ++cell)
                if (dist[cell][steps] != Integer.MAX_VALUE) {
                    for (int nextCell = 1; nextCell <= n * n; ++nextCell)
                        if (grid[nextCell / n][nextCell % n] > grid[cell / n][cell % n]) {
                            int nextSteps = steps + 1;
                            if (nextSteps > k) break;
                            dist[nextCell][nextSteps] = Math.min(dist[nextCell][nextSteps], dist[cell][steps] + grid[nextCell / n][nextCell % n]);
                        }
                }

C:
        int minDist = Integer.MAX_VALUE;
        for (int cell = 1; cell <= n * n; ++cell)
            minDist = Math.min(minDist, dist[cell][k]);

D:
        if (minDist == Integer.MAX_VALUE) return new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        int cell = 0;
        for (int i = k; i >= 0; --i)
            for (int j = 1; j <= n * n; ++j)
                if (dist[j][i] + grid[j / n][j % n] == minDist) {
                    cell = j;
                    break;
                }
        while (k >= 0) {
            path.add(grid[cell / n][cell % n]);
            int nextCell = 0;
            for (int i = 0; i <= k; ++i)
                if (dist[cell][i] + grid[cell / n][cell % n] == minDist) {
                    k = i;
                    break;
                }
            cell = nextCell;
        }
        return path;
   