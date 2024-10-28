        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        Collections.sort(result, new Comparator<List<Integer>>() {
            public int compare(List<Integer> l1, List<Integer> l2) {
                if (l1.get(0).equals(l2.get(0))) {
                    return Integer.compare(l2.get(1), l1.get(1));
                } else {
                    return Integer.compare(l1.get(0), l2.get(0));
                }
            }
        });
        return result;
    }
}

