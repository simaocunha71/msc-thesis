        if (n <= 1) {
            return 0;
        } else if (n == 2) {
            return 1;
        } else {
            int[] memo = new int[n + 1];
            memo[1] = memo[2] = 0;
            memo[2] = 1;
            for (int i = 3; i <= n; i++) {
                memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3];
            }
            return memo[n];
        }
    }
}

