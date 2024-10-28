        int n = grid.size();
        int[][] directions = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        boolean[][] visited = new boolean[n][n];
        List<Integer> res = new ArrayList<>();
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                visited[i][j] = true;
                dfs(grid, i, j, k - 1, visited, new ArrayList<Integer>() {{add(grid.get(i).get(j));}}, n, min, res);
                visited[i][j] = false;
            }
        }
        return res;
    }

    private void dfs(List<List<Integer>> grid, int x, int y, int k, boolean[][] visited, List<Integer> path, int n, int min, List<Integer> res) {
        if (k == 0) {
            int sum = path.stream().mapToInt(Integer::intValue).sum();
            if (sum < min) {
                min = sum;
                res.clear();
                res.addAll(path);
            }
            return;
        }
        for (int[] dir : directions) {
            int newX = x + dir[0], newY = y + dir[1];
            if (newX < 0 || newX >= n || newY < 0 || newY >= n || visited[newX][newY]) {
                continue;
            }
            path.add(grid.get(newX).get(newY));
            visited[newX][newY] = true;
            dfs(grid, newX, newY, k - 1, visited, path, n, min, res);
            visited[newX][newY] = false;
            path.remove(path.size() - 1);
        }
    }
}

Here, the `minPath` method is used to find the minimum path in the grid of size N*N for length k. This is achieved