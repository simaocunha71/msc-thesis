        int N = grid.size();
        int[][] grid_with_numbers = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                grid_with_numbers[i][j] = grid.get(i).get(j);
            }
        }
        int[][] grid_with_numbers_sorted = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                grid_with_numbers_sorted[i][j] = grid_with_numbers[i][j];
            }
        }
        Arrays.sort(grid_with_numbers_sorted);

        List<Integer> result = new ArrayList<>();
        int current_grid_value = -1;
        int current_grid_index = -1;
        int current_grid_value_sorted = -1;

        for (int i = 0; i < k; i++) {
            for (int j = 0; j < N; j++) {
                for (int l = 0; l < N; l++) {
                    if (grid_with_numbers[j][l] == current_grid_value_sorted) {
                        current_grid_index = j;
                        current_grid_value = grid_with_numbers[j][l];
                    }
                }
            }
            result.add(current_grid_value);
            grid_with_numbers_sorted[current_grid_index][current_grid_index] = Integer.MAX_VALUE;
            current_grid_value_sorted += 1;
        }

        return result;
    }
}

