        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        result.sort(Comparator.comparing((List<Integer> p) -> p.get(0)).thenComparing((List<Integer> p) -> p.get(1), Comparator.reverseOrder()));
        return result;
    }
}

