        List<List<Integer>> result = new ArrayList<>();

        for (int row = 0; row < lst.size(); row++) {
            List<Integer> row_lst = lst.get(row);
            int row_length = row_lst.size();

            for (int col = 0; col < row_length; col++) {
                if (row_lst.get(col) == x) {
                    result.add(Arrays.asList(row, col));
                }
            }
        }

        result.sort(new Comparator<List<Integer>>() {
            @Override
            public int compare(List<Integer> o1, List<Integer> o2) {
                return o1.get(0) == o2.get(0) ?
                        -1 * (o1.get(1) - o2.get(1)) : o1.get(0) - o2.get(0);
            }
        });
        return result;
    }
}

