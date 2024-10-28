        int n = grid.size();
        int[][] dp = new int[n][n];
        int[][] dq = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int cur = grid.get(i).get(j);
                dp[i][j] = cur;
                dq[i][j] = cur;
            }
        }

        int[] di = new int[]{0, 0, 1, -1};
        int[] dj = new int[]{1, -1, 0, 0};
        int[][] dir = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        List<int[]> path = new ArrayList<>();
        int[] cur = new int[]{0, 0};
        path.add(cur);
        Set<Integer> vis = new HashSet<>();
        vis.add(cur[0]);
        vis.add(cur[1]);
        for (int i = 0; i < k; i++) {
            List<int[]> next = new ArrayList<>();
            int[][] tmp = new int[n][n];
            for (int[] p : path) {
                int x = p[0];
                int y = p[1];
                for (int[] d : dir) {
                    int nx = x + d[0];
                    int ny = y + d[1];
                    if (nx >= 0 && nx < n && ny >= 0 && ny < n && !vis.contains(nx) && !vis.contains(ny)) {
                        int val = dp[nx][ny];
                        next.add(new int[]{nx, ny});
                        vis.add(nx);
                        vis.add(ny);
                        tmp[nx][ny] = val;
                    }
                }
            }
            path = next;
            for (int[] p : path) {
                dq[p[0]][p[1