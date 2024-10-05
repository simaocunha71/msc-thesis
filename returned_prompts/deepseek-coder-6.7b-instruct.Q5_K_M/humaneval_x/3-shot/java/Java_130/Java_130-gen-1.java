        List<Integer> result = new ArrayList<>();
        if (n < 0) return result;

        int[] memo = new int[n+2];
        memo[1] = 3;
        if (n > 0) {
            memo[2] = 2;
            for (int i = 3; i <= n+1; i++) {
                memo[i] = memo[i-1] + memo[i-2] + (i%2 == 0 ? 1 : memo[i+1]);
            }
        }

        for (int i = 1; i <= n+1; i++) {
            result.add(memo[i]);
        }
        return result;
    }
}

