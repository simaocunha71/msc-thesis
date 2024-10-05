        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        Collections.sort(result, new Comparator<List<Integer>>() {
            public int compare(List<Integer> a, List<Integer> b) {
                return a.get(0).compareTo(b.get(0));
            }
        });
        for (List<Integer> coord : result) {
            Collections.sort(Arrays.asList(coord.get(1), coord.get(0)), new Comparator<Integer>() {
                public int compare(Integer a, Integer b) {
                    return b.compareTo(a);
                }
            });
        }
        return result;
    }
}