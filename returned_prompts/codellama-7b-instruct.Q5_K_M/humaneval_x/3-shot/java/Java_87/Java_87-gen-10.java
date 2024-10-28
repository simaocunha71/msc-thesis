        List<List<Integer>> result = new ArrayList<>();
        if (lst.size() == 0) return result;

        List<Integer> row_indexes = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    row_indexes.add(i);
                    break;
                }
            }
        }

        // sort rows by ascending index
        Collections.sort(row_indexes);

        // for each row, sort its columns by descending index
        for (int i = 0; i < row_indexes.size(); i++) {
            List<Integer> columns = new ArrayList<>();
            int row_index = row_indexes.get(i);
            for (int j = 0; j < lst.get(row_index).size(); j++) {
                if (lst.get(row_index).get(j) == x) {
                    columns.add(j);
                    break;
                }
            }
            Collections.sort(columns, Collections.reverseOrder());
            result.add(columns);
        }
        return result;
    }
}

