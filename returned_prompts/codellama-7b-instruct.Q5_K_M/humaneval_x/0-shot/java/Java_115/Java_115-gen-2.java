        int n = grid.size();
        int m = grid[0].size();
        int[] dp = new int[n];
        int[] prev = new int[n];
        int[] next = new int[n];
        Arrays.fill(dp, 1);
        Arrays.fill(prev, 0);
        Arrays.fill(next, 0);
        for (int i = 0; i < m; i++) {
            int left = 0;
            int right = n - 1;
            while (left <= right) {
                int mid = (left + right) / 2;
                int p = mid;
                int q = mid + 1;
                while (p >= 0) {
                    if (grid[p][i] == 1) {
                        if (dp[p] <= capacity) {
                            break;
                        }
                    }
                    p--;
                }
                while (q < n) {
                    if (grid[q][i] == 1) {
                        if (dp[q] <= capacity) {
                            break;
                        }
                    }
                    q++;
                }
                if (p < 0 || q >= n) {
                    left = mid + 1;
                } else if (dp[p] + dp[q] <= capacity) {
                    dp[p] = dp[p] + dp[q];
                    prev[q] = p;
                    next[p] = q;
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] > capacity) {
                return -1;
            }
            ans = Math.max(ans, dp[i]);
        }
        return ans;
    }
}
