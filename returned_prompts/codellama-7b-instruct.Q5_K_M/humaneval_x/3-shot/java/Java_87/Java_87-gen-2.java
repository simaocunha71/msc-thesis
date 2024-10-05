        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    List<Integer> coordinate = new ArrayList<>();
                    coordinate.add(i);
                    coordinate.add(j);
                    result.add(coordinate);
                }
            }
        }
        result.sort((l1, l2) -> l1.get(0) == l2.get(0) ? l2.get(1) - l1.get(1) : l1.get(0) - l2.get(0));
        return result;
    }
}

