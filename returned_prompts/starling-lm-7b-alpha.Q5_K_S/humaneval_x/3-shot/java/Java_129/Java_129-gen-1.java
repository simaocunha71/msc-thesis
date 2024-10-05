        List<Integer> result = new ArrayList<>();
        int N = grid.size();
        int[][] directions = new int[][] {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int[][] lookup = new int[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(lookup[i], Integer.MAX_VALUE);
        }
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (lookup[r][c] == Integer.MAX_VALUE) {
                    LinkedList<Integer> queue = new LinkedList<>();
                    queue.add(r);
                    queue.add(c);
                    lookup[r][c] = grid[r][c];
                    while (!queue.isEmpty()) {
                        int r_index = queue.removeFirst();
                        int c_index = queue.removeFirst();
                        for (int[] d : directions) {
                            int r_n = r_index + d[0];
                            int c_n = c_index + d[1];
                            if (r_n >= 0 && r_n < N && c_n >= 0 && c_n < N && lookup[r_n][c_n] == Integer.MAX_VALUE) {
                                queue.add(r_n);
                                queue.add(c_n);
                                lookup[r_n][c_n] = grid[r_n][c_n];
                            }
                        }
                    }
                }
            }
        }
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                int next_number = lookup[r][c] + k;
                if (next_number % N == 0) {
                    next_number = N;
                }
                result.add(next_number % N);
            }
        }
        return result;
