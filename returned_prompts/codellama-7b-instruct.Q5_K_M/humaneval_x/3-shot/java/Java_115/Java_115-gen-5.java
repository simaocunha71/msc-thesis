        int result = 0;
        // number of rows
        int n = grid.size();
        // number of columns
        int m = grid.get(0).size();
        // number of water units in each well
        int[][] well_count = new int[n][m];

        // count number of water units in each well
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid.get(i).get(j) == 1) {
                    well_count[i][j] = 1;
                }
            }
        }

        // count number of water units in each row
        int[] row_count = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                row_count[i] += well_count[i][j];
            }
        }

        // count number of water units in each column
        int[] col_count = new int[m];
        for (int j = 0; j < m; j++) {
            for (int i = 0; i < n; i++) {
                col_count[j] += well_count[i][j];
            }
        }

        // find minimum row and column with water units
        int min_row = 0;
        int min_col = 0;
        for (int i = 0; i < n; i++) {
            if (row_count[i] < row_count[min_row]) {
                min_row = i;
            }
        }
        for (int j = 0; j < m; j++) {
            if (col_count[j] < col_count[min_col]) {
                min_col = j;
            }
        }

        // fill wells from left to right
        while (min_col < m && min_row < n) {
            int fill_count = Math.min(capacity - well_count[min_row][min_col],
                    col