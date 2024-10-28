        if (n == 0) return 0;
        if (n == 1) return 1;

        int[] memo = new int[n+1];
        memo[0] = 0;
        memo[1] = 1;

        for (int i = 2; i <= n; i++) {
            memo[i] = memo[i-2] + memo[i-1];
        }
        return memo[n];
    }
}

