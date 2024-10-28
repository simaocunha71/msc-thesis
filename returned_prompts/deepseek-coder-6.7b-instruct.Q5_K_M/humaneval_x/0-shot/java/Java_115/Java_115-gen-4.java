        int rows = grid.size(), cols = grid.get(0).size(), total = 0;
        int[] arr = new int[rows * cols];
        for(int i = 0; i < rows; i++)
            for(int j = 0; j < cols; j++)
                if(grid.get(i).get(j) == 1) {
                    arr[i * cols + j] = Integer.MAX_VALUE;
                    total++;
                }
        int[] dp = new int[total];
        Arrays.sort(arr);
        for(int i = 0; i < total; i++) {
            int x = arr[i] / cols, y = arr[i] % cols;
            dp[i] = x + 1;
            if(y > 0 && dp[i] < dp[(x - 1) * cols + y - 1] + 1)
                dp[i] = dp[(x - 1) * cols + y - 1] + 1;
            if(y < cols - 1 && dp[i] < dp[(x - 1) * cols + y + 1] + 1)
                dp[i] = dp[(x - 1) * cols + y + 1] + 1;
        }
        int res = 0, p = total - 1;
        for(int i = cols - 1; i >= 0; i--) {
            while(p >= 0 && dp[p] > i) p--;
            if(p < 0) break;
            res += dp[p];
        }
        return res;
    }
}

I:









































































































