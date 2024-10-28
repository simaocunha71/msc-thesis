        int n = arr.size();
        int[] dp = new int[n];
        int[] left = new int[n];
        int[] right = new int[n];

        for (int i = 0; i < n; i++) {
            int min = Integer.MAX_VALUE;
            for (int j = 0; j < i; j++) {
                min = Math.min(min, dp[j]);
            }
            for (int j = i + 1; j < n; j++) {
                min = Math.min(min, dp[j]);
            }
            min++;
            dp[i] = min;
        }
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            min = Math.min(min, dp[i]);
        }
        return min;
    }
}

