        int num_fills = 0;
        int num_rows = grid.size();
        int num_cols = grid.get(0).size();

        for (int i = 0; i < num_rows; i++) {
            int curr_row_sum = 0;
            for (int j = 0; j < num_cols; j++) {
                curr_row_sum += grid.get(i).get(j);
            }
            if (curr_row_sum <= capacity) {
                num_fills += 1;
            }
        }

        return num_fills;
    }
}
