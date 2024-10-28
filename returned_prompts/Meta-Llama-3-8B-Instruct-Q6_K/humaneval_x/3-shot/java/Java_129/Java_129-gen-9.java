        int n = grid.size();
        List<Integer> result = new ArrayList<>();

        // Start from the first cell
        minPath(grid, 0, 0, k, result);
        return result;
    }

    private void minPath(List<List<Integer>> grid, int i, int j, int k, List<Integer> result) {
        if (k == 0) {
            return;
        }

        // Add the current cell value to the result
        result.add(grid.get(i).get(j));

        // Explore the neighbors
        for (int di = -1; di <= 1; di++) {
            for (int dj = -1; dj <= 1; dj++) {
                if (di == 0 && dj == 0) continue;
                int ni = i + di;
                int nj = j + dj;

                if (ni >= 0 && ni < grid.size() && nj >= 0 && nj < grid.get(0).size()) {
                    minPath(grid, ni, nj, k - 1, result);
                }
            }
        }
    }
}
