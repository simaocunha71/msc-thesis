        int n = grid.size();
        int m = grid.get(0).size();
        int[][] grid_copy = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                grid_copy[i][j] = grid.get(i).get(j);
            }
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                queue.add(grid_copy[i][j]);
            }
        }

        List<Integer> result = new ArrayList<>();
        while (k > 0) {
            int index = queue.remove();
            result.add(index);
            if (index - 1 >= 0) queue.add(index - 1);
            if (index + 1 < n * m) queue.add(index + 1);
            if (k == 1) break;
            k--;
        }

        return result;
    }
}

