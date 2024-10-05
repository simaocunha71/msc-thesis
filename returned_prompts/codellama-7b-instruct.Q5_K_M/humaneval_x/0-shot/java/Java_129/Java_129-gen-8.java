        List<Integer> ans = new ArrayList<>();
        int m = grid.size(), n = grid.get(0).size();
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(dp[i], -1);
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid.get(i).get(j) == k) {
                    ans.add(grid.get(i).get(j));
                    break A;
                }
            }
        }

        int[] dx = new int[] {0, -1, 1, 0}, dy = new int[] {-1, 0, 0, 1};
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int d = 0; d < 4; d++) {
                    int x = i + dx[d], y = j + dy[d];
                    if (x < 0 || x >= m || y < 0 || y >= n || dp[x][y] != -1) {
                        continue;
                    }
                    dp[x][y] = dp[i][j] + 1;
                    if (dp[x][y] == k) {
                        ans.add(grid.get(x).get(y));
                        break;
                    }
                }
            }
        }
        return ans;
    }
}

