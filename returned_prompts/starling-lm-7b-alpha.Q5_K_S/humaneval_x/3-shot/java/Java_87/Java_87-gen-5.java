        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        Collections.sort(result, new Comparator<List<Integer>>() {
            @Override
            public int compare(List<Integer> o1, List<Integer> o2) {
                if (o1.get(0) == o2.get(0)) {
                    return Integer.compare(o2.get(1), o1.get(1));
                }
                return Integer.compare(o1.get(0), o2.get(0));
            }
        });
        return result;
    }
}

