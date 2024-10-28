        List<Integer> result = new ArrayList<>();
        int min = Integer.MAX_VALUE;
        int row = 0;
        int col = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(i).size(); j++) {
                if (grid.get(i).get(j) < min) {
                    min = grid.get(i).get(j);
                    row = i;
                    col = j;
                }
            }
        }
        result.add(min);
        int i = 0;
        while (i < k - 1) {
            if (row == 0) {
                if (col == 0) {
                    result.add(grid.get(row + 1).get(col));
                    row += 1;
                    i += 1;
                } else if (col == grid.size() - 1) {
                    result.add(grid.get(row).get(col - 1));
                    col -= 1;
                    i += 1;
                } else {
                    if (grid.get(row + 1).get(col) < grid.get(row).get(col - 1)) {
                        result.add(grid.get(row + 1).get(col));
                        row += 1;
                        i += 1;
                    } else {
                        result.add(grid.get(row).get(col - 1));
                        col -= 1;
                        i += 1;
                    }
                }
            } else if (row == grid.size() - 1) {
                if (col == 0) {
                    result.add(grid.get(row - 1).get(col));
                    row -= 1;
                    i += 1;
                } else if (col == grid.size() - 1) {
                    result.add(grid.get(row).get(col - 1));
                    col -= 1;
                    i += 1;
                } else {
                    if (grid.get(row - 1).get(col) < grid.get(row).get(col - 1)) {
                        result.add(grid.get(row - 1).get(col));
                        row -= 1;
                        i += 1;
                    } else {
                        result.add(grid.get(row).get(col - 1));
                        col -= 1;
                        i += 1;
                    }
                }
            } else {
                if (col == 0) {
                    if (grid.get(row - 1).get(col) < grid.get(row + 1).get