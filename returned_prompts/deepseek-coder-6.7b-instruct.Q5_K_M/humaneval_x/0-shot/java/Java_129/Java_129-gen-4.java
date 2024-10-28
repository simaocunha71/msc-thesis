        List<Integer> ans = new ArrayList<>();
        int n = grid.size();
        int[][][] dp = new int[k+1][n][n];
        int[][] dir = {{0,1},{1,0},{0,-1},{-1,0}};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dp[1][i][j] = grid.get(i).get(j);
            }
        }

        for (int steps = 2; steps <= k; steps++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    int min = Integer.MAX_VALUE;
                    for (int[] d : dir) {
                        int x = i + d[0], y = j + d[1];
                        if (x >= 0 && x < n && y >= 0 && y < n) {
                            min = Math.min(min, dp[steps-1][x][y]);
                        }
                    }
                    dp[steps][i][j] = min == Integer.MAX_VALUE ? min : grid.get(i).get(j) + min;
                }
            }
        }

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[k][i][j] < min) {
                    min = dp[k][i][j];
                }
            }
        }

        for (int steps = k; steps > 0; steps--) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dp[steps][i][j] == min) {
                        ans.add(grid.get(i).get(j));
                        min -= grid.get(i).get(j);
                        for (int[] d : dir) {