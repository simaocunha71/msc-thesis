        int n = grid.size();
        int m = grid.get(0).size();

        int[][] grid_copy = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                grid_copy[i][j] = grid.get(i).get(j);
            }
        }

        int result = 0;
        while (true) {
            boolean can_fill = false;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (grid_copy[i][j] == 1) {
                        can_fill = true;
                        grid_copy[i][j] = 0;

                        int current_bucket = capacity;
                        while (current_bucket > 0 &&
                            is_valid(grid_copy, i + 1, j, current_bucket)) {
                            grid_copy[i + 1][j] -= current_bucket;
                            current_bucket = current_bucket - 1;
                        }

                        while (current_bucket > 0 &&
                            is_valid(grid_copy, i - 1, j, current_bucket)) {
                            grid_copy[i - 1][j] -= current_bucket;
                            current_bucket = current_bucket - 1;
                        }

                        while (current_bucket > 0 &&
                            is_valid(grid_copy, i, j + 1, current_bucket)) {
                            grid_copy[i][j + 1] -= current_bucket;
                            current_bucket = current_bucket - 1;
                        }

                        while (current_bucket > 0 &&
                            is_valid(grid_copy, i, j - 1, current_bucket)) {
                            grid_copy[i][j - 1] -= current_bucket;
                            current_bucket = current_bucket - 1;
                        }
                    }
                }