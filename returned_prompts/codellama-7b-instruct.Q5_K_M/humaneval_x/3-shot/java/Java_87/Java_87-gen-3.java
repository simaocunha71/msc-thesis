        List<List<Integer>> result = new ArrayList<>();
        int row = 0;
        for (List<Integer> row_lst : lst) {
            for (int i = 0; i < row_lst.size(); i++) {
                if (row_lst.get(i) == x) {
                    result.add(Arrays.asList(row, i));
                }
            }
            row += 1;
        }
        result.sort(Comparator.comparingInt(l -> l.get(0)));
        for (List<Integer> lst1 : result) {
            lst1.sort(Comparator.comparingInt(x1 -> -x1).thenComparingInt(x1 -> x1));
        }
        return result;
    }
}

