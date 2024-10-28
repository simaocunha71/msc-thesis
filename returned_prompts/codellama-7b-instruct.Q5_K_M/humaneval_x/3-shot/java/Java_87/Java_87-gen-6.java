        List<List<Integer>> result = new ArrayList<>();

        if (lst.size() == 0) return result;

        int row_count = 0;
        int col_count = lst.get(0).size();

        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    result.add(new ArrayList<>(Arrays.asList(i, j)));
                }
            }
        }

        Collections.sort(result, (List<Integer> a, List<Integer> b) -> {
            if (a.get(0) < b.get(0)) return -1;
            if (a.get(0) > b.get(0)) return 1;
            if (a.get(1) > b.get(1)) return -1;
            if (a.get(1) < b.get(1)) return 1;
            return 0;
        });
        return result;

    }
}

