        int N = grid.size();
        List<List<Integer>> memo = new ArrayList<>(N);
        for (int i = 0; i < N; i++) {
            memo.add(new ArrayList<>(N));
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                memo.get(i).add(0);
            }
        }
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int x = dfs(grid, i, j, 0, memo);
                min = Math.min(min, x);
            }
        }
        return result;
    }

    private int dfs(List<List<Integer>> grid, int i, int j, int k, List<List<Integer>> memo) {
        if (k == grid.size() * grid.size()) {
            return 0;
        }
        if (memo.get(i).get(j) != 0) {
            return memo.get(i).get(j);
        }
        int result = Integer.MAX_VALUE;
        int current = grid.get(i).get(j);
        if (i > 0) {
            result = Math.min(result, current + dfs(grid, i - 1, j, k + 1, memo));
        }
        if (i < grid.size() - 1) {
            result = Math.min(result, current + dfs(grid, i + 1, j, k + 1, memo));
        }
        if (j > 0) {
            result = Math.min(result, current + dfs(grid, i, j - 1, k + 1, memo));
        }
        if (j < grid.size() - 1) {
            result = Math.min(result, current + dfs(grid, i, j + 1, k + 1, memo));
        }
        memo.get(i).set(j, result);
        return result;
    }
}

