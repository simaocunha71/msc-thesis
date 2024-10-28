        List<List<Integer>> result = new ArrayList<>();
        int row_count = 0;
        int column_count = 0;
        for (List<Integer> row : lst) {
            column_count = row.size();
            for (int i = 0; i < row.size(); i++) {
                if (row.get(i) == x) {
                    result.add(Arrays.asList(row_count, i));
                }
            }
            row_count += 1;
        }
        return result;
    }
}

