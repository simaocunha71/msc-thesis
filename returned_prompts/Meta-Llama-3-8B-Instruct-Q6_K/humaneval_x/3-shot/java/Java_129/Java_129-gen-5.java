        int N = grid.size();
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (k > 0) {
                    List<Integer> path = new ArrayList<>();
                    dfs(grid, i, j, k, dirs, path);
                    if (res.isEmpty() || path.get(path.size() - 1) < res.get(res.size() - 1)) {
                        res = path;
                    }
                }
            }
        }
        return res;
    }

    private void dfs(List<List<Integer>> grid, int i, int j, int k, int[][] dirs, List<Integer> path) {
        if (k == 0) {
            return;
        }
        path.add(grid.get(i).get(j));
        for (int[] dir : dirs) {
            int ni = i + dir[0];
            int nj = j + dir[1];
            if (ni >= 0 && ni < grid.size() && nj >= 0 && nj < grid.get(0).size()) {
                dfs(grid, ni, nj, k - 1, dirs, path);
            }
        }
        path.remove(path.size() - 1);
    }
}