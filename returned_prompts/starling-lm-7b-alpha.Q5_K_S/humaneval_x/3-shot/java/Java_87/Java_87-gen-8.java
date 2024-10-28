        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            List<Integer> row = lst.get(i);
            for (int j = 0; j < row.size(); j++) {
                if (row.get(j) == x) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        Collections.sort(result, (a, b) -> Integer.compare(a.get(0), b.get(0)));
        Collections.sort(result, (a, b) -> Integer.compare(b.get(1), a.get(1)));
        return result;
    }
}


