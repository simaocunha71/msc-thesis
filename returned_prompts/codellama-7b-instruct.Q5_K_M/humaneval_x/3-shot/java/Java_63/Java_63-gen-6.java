        if (n <= 1) return 0;

        if (n == 2) return 1;

        int[] memo = new int[n];
        memo[0] = 0;
        memo[1] = 0;
        memo[2] = 1;

        for (int i = 3; i <= n; i++) {
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3];
        }
        return memo[n];
    }
}

