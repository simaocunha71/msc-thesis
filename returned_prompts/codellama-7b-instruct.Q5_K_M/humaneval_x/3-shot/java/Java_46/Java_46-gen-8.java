        int[] memo = new int[n+1];
        memo[0] = 0;
        memo[1] = 0;
        memo[2] = 2;
        memo[3] = 0;

        for (int i = 4; i <= n; i++) {
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3] + memo[i-4];
        }
        return memo[n];
    }
}

