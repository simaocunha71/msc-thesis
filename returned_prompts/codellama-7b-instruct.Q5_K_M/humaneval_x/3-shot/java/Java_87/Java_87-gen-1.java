        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current_row = new ArrayList<>();
        int current_row_index = -1;
        int current_column_index = -1;

        for (List<Integer> row : lst) {
            current_row.clear();
            current_row_index += 1;

            for (int column : row) {
                current_column_index += 1;
                if (column == x) {
                    current_row.add(current_row_index);
                    current_row.add(current_column_index);
                    result.add(current_row);
                }
            }
        }
        return result;
    }
}

