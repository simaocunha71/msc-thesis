        int N = grid.size();
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int[][] visited = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                visited[i][j] = -1;
            }
        }

        Queue<Integer> queue = new LinkedList<>();
        queue.add(grid.get(0).get(0));
        visited[0][0] = 0;
        List<Integer> result = new ArrayList<>();
        int length = k;

        while (length > 0 && !queue.isEmpty()) {
            List<Integer> next_queue = new ArrayList<>();
            while (!queue.isEmpty() && length > 0) {
                int current_cell = queue.poll();
                result.add(current_cell);
                length -= 1;

                for (int[] direction : directions) {
                    int r = current_cell / N;
                    int c = current_cell % N;
                    int new_r = r + direction[0];
                    int new_c = c + direction[1];

                    if (new_r < 0 || new_r >= N || new_c < 0 || new_c >= N) {
                        continue;
                    }

                    int new_cell = new_r * N + new_c;

                    if (visited[new_r][new_c] != -1) {
                        continue;
                    }

                    if (length == 0) {
                        continue;
                    }

                    visited[new_r][new_c] = visited[r][c] + 1;
                    next_queue.add(new_cell);
                }
            }

            queue = next_queue;
        }

        return result;
    }
}

