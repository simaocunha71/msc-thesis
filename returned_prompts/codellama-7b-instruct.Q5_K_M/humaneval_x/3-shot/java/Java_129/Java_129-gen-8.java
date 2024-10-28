        int rows = grid.size();
        int cols = grid.get(0).size();
        int[][] dp = new int[rows][cols];
        int[][] dirs = new int[][] { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                dp[i][j] = grid.get(i).get(j);
            }
        }

        for (int i = 1; i < k; i++) {
            for (int i = 1; i < rows; i++) {
                for (int j = 1; j < cols; j++) {
                    dp[i][j] = Math.min(
                        dp[i - 1][j] + grid.get(i)[j],
                        Math.min(
                            dp[i][j - 1] + grid.get(i)[j],
                            dp[i - 1][j - 1] + grid.get(i)[j]));
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        int r = 0;
        int c = 0;
        while (dp[r][c] != 0) {
            result.add(grid.get(r).get(c));
            int[] dr = { -1, 1, 0, 0 };
            int[] dc = { 0, 0, -1, 1 };
            r += dr[dp[r][c]];
            c += dc[dp[r][c]];
        }
        return result;
    }
}

