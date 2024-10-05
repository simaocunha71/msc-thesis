        int N = grid.size();
        List<Integer> result = new ArrayList<>();
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        boolean[][] visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (grid.get(i).get(j) == 1) {
                    result.add(grid.get(i).get(j));
                    visited[i][j] = true;
                    for (int step = 0; step < k; step++) {
                        boolean found = false;
                        for (int[] direction : directions) {
                            int new_i = i + direction[0];
                            int new_j = j + direction[1];
                            if (new_i >= 0 && new_i < N && new_j >= 0 && new_j < N && !visited[new_i][new_j]) {
                                if (grid.get(new_i).get(new_j) < grid.get(i).get(j)) {
 result.add(grid.get(new_i).get(new_j));
 visited[new_i][new_j] = true;
 found = true;
 break;
                                }
                            }
                        }
                        if (!found) break;
                    }
                    result.add(grid.get(i).get(j));
                    visited[i][j] = false;
                }
            }
        }
        return result;
    }
}