        List<Integer> result = new ArrayList<>();
        int N = grid.size();
        int[][] memo = new int[N][N];

        // Initialize all cells to infinity
        for (int i = 0; i < N; i++) {
            Arrays.fill(memo[i], Integer.MAX_VALUE);
        }

        // Base case
        memo[0][0] = grid.get(0).get(0);
        result.add(memo[0][0]);

        // Fill the grid with the minimum value of the cell and its neighbors
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < N; j++) {
                memo[i][j] = Math.min(memo[i - 1][j], memo[i][j - 1]) + grid.get(i).get(j);
                result.add(memo[i][j]);
            }
        }

        // Find the kth smallest value in the list
        result = result.subList(0, k);
        Collections.sort(result);
        return result;
    }
}

