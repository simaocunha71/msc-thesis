        int n = grid.size();
        int[][] dp = new int[n * n + 1][k + 1];
        for (int i = 0; i <= n * n; i++) {
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        }
        dp[0][0] = 0;
        int[][] dir = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] != b[2] ? a[2] - b[2] : a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        pq.offer(new int[]{0, 0, grid.get(0).get(0)});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            for (int[] d : dir) {
                int x = cur[0] + d[0], y = cur[1] + d[1];
                if (x >= 0 && x < n && y >= 0 && y < n) {
                    int nxtVal = cur[2] + grid.get(x).get(y);
                    for (int l = 1; l <= k; l++) {
                        if (nxtVal < dp[l][x * n + y]) {
                            dp[l][x * n + y] = nxtVal;
                            pq.offer(new int[]{x, y, nxtVal});
                        }
                    }
                }
            }
        }
        List<Integer> res = new ArrayList<>();
        for (int i = 1; i <= k; i++) {
            int min = Integer.MAX_VALUE, idx = -1;
            for (int j = 0; j < n * n; j++) {
                if (dp[i][j] < min) {
                    min = dp[i][j];
                    idx = j;
                }
            }
           