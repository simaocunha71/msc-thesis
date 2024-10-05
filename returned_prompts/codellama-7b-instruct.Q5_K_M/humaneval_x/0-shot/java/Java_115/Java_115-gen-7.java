        int max_water = 0;
        int row = grid.size();
        int col = grid.get(0).size();
        int[][] dp = new int[row][col];
        int[][] memo = new int[row][col];
        int[][] bucket = new int[row][col];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                memo[i][j] = -1;
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid.get(i).get(j) == 1) {
                    bucket[i][j] = 1;
                    max_water++;
                }
            }
        }

        int water = max_water;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid.get(i).get(j) == 1) {
                    if (j - 1 >= 0 && bucket[i][j - 1] > 0) {
                        bucket[i][j - 1]--;
                        water--;
                    } else if (i - 1 >= 0 && bucket[i - 1][j] > 0) {
                        bucket[i - 1][j]--;
                        water--;
                    }
                }
            }
        }

        int fill_times = 0;

        while (water > 0) {
            int next_row = -1;
            int next_col = -1;
            int next_capacity = -1;
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col; j++) {
                    if (bucket[i][j] > 0) {
                        if (next_capacity == -1 || next_capacity > bucket[i][j])