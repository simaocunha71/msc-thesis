        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < lst.size(); i++) {
            List<List<Integer>> coordinates = new ArrayList<>();
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    coordinates.add(Arrays.asList(i, j));
                }
            }
            Collections.sort(coordinates, (a, b) -> {
                if (a.get(0) == b.get(0)) {
                    return b.get(1) - a.get(1);
                } else {
                    return a.get(0) - b.get(0);
                }
            });
            result.addAll(coordinates);
        }
        return result;
    }
}

