    public int smallestChange(List<Integer> arr) {
        int n = arr.size();
        int[] dp = new int[n];
        dp[0] = 0;
        for (int i = 1; i < n; i++) {
            dp[i] = dp[i - 1] + 1;
        }
        for (int i = n - 2; i >= 0; i--) {
            if (arr.get(i).equals(arr.get(n - i - 1))) {
                dp[i] = Math.min(dp[i], dp[i + 1]);
            }
        }
        return dp[0];
    }