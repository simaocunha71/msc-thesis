        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            List<Integer> row = lst.get(i);
            for (int j = row.size() - 1; j >= 0; j--) {
                if (row.get(j) == x) {
                    List<Integer> coordinates = new ArrayList<>();
                    coordinates.add(i);
                    coordinates.add(j);
                    result.add(coordinates);
                }
            }
        }
        return result;
    }
}

