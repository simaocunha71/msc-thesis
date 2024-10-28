        int n = grid.size();
        int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid.get(i).get(j) == 1) {
                    dfs(grid, i, j, k, res, dir);
                }
            }
        }
        return res;
    }

    private void dfs(List<List<Integer>> grid, int i, int j, int k, List<Integer> res, int[][] dir) {
        int n = grid.size();
        if (k == 0) {
            res.add(grid.get(i).get(j));
            return;
        }
        for (int[] d : dir) {
            int ni = i + d[0], nj = j + d[1];
            if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                if (grid.get(ni).get(nj) > grid.get(i).get(j)) {
                    dfs(grid, ni, nj, k - 1, res, dir);
                }
            }
        }
    }
}
