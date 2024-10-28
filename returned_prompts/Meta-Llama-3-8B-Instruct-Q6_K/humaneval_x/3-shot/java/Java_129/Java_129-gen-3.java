        int n = grid.size();
        List<Integer> result = new ArrayList<>();
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int[][] visited = new int[n][n];
        int[][] order = new int[n][n];
        int minVal = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid.get(i).get(j) < minVal) {
                    minVal = grid.get(i).get(j);
                }
                order[i][j] = grid.get(i).get(j);
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                visited[i][j] = 0;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] == 0) {
                    DFS(grid, visited, order, directions, i, j, k, result);
                }
            }
        }
        return result;
    }

    private void DFS(List<List<Integer>> grid, int[][] visited, int[][] order, int[][] directions, int i, int j, int k, List<Integer> result) {
        int n = grid.size();
        if (k == 0) {
            return;
        }
        for (int d = 0; d < 4; d++) {
            int ni = i + directions[d][0];
            int nj = j + directions[d][1];
            if (ni >= 0 && ni < n && nj >= 0 && nj < n && visited[ni][nj] == 0) {
                visited[ni][nj] = 1;
                result.add(order[ni][nj]);
                DFS(grid, visited, order, directions, ni, nj, k - 1, result);
                visited[ni][nj] = 0;
                result.remove(result.size() - 1);
            }
        }
    }
} 