        int N = grid.size();
        int[][] path_lengths = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                path_lengths[i][j] = Integer.MAX_VALUE;
            }
        }

        LinkedList<Integer> path = new LinkedList<>();
        path.add(grid.get(0).get(0));
        path_lengths[0][0] = 1;
        while (path.size() < k) {
            List<Integer> next_cells = new ArrayList<>();
            for (int i : path) {
                int x = i / N;
                int y = i % N;
                next_cells.add(grid.get(x - 1).get(y));
                next_cells.add(grid.get(x).get(y - 1));
                next_cells.add(grid.get(x + 1).get(y));
                next_cells.add(grid.get(x).get(y + 1));
            }
            Collections.sort(next_cells);
            int index = 0;
            while (index < next_cells.size() && path_lengths[next_cells.get(index) / N][next_cells.get(index) % N] < Integer.MAX_VALUE) {
                index += 1;
            }
            path.add(next_cells.get(index));
            path_lengths[next_cells.get(index) / N][next_cells.get(index) % N] = path.size();
        }
        Collections.sort(path);
        return path;
    }
}


```