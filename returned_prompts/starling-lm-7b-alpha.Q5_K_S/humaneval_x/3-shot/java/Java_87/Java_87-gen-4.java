        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        result.sort((a, b) -> Integer.compare(a.get(0), b.get(0)));
        result.forEach((a) -> a.sort((c, d) -> Integer.compare(d, c)));

        return result;
    }
}

