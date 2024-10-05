        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            List<Integer> row = lst.get(i);
            for (int j = row.size() - 1; j >= 0; j--) {
                if (row.get(j) == x) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        return result;
    }
}

