        int n = grid.size();
        List<Integer> result = new ArrayList<>();
        List<List<Integer>> grid_list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            grid_list.add(grid.get(i));
        }
        result.add(grid_list.get(0).get(0));
        result.add(grid_list.get(0).get(1));

        for (int i = 1; i < k - 1; i++) {
            List<List<Integer>> grid_next = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                List<Integer> grid_next_row = new ArrayList<>();
                grid_next_row.add(grid_list.get(j).get(0));
                grid_next_row.add(grid_list.get(j).get(1));
                grid_next_row.add(grid_list.get(j).get(2));

                if (j < n - 1) {
                    grid_next_row.add(grid_list.get(j + 1).get(2));
                }

                if (j > 0) {
                    grid_next_row.add(grid_list.get(j - 1).get(2));
                }

                grid_next.add(grid_next_row);
            }
            grid_list = grid_next;
            result.add(grid_list.get(0).get(0));
            result.add(grid_list.get(0).get(1));
        }

        result.add(grid_list.get(n - 1).get(n - 1));
        return result;
    }
}


```