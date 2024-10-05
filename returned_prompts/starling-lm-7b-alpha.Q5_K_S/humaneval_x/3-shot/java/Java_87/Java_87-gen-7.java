        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        result.sort((l1, l2) -> Integer.compare(l1.get(0), l2.get(0)));
        result.sort((l1, l2) -> Integer.compare(l2.get(1), l1.get(1)));
        return result;
    }
}

