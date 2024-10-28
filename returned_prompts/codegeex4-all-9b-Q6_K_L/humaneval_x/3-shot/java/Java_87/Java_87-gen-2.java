        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            List<Integer> row = lst.get(i);
            for (int j = 0; j < row.size(); j++) {
                if (row.get(j) == x) {
                    List<Integer> coordinate = new ArrayList<>();
                    coordinate.add(i);
                    coordinate.add(j);
                    result.add(coordinate);
                }
            }
        }
        result.sort((a, b) -> {
            if (a.get(0) != b.get(0)) {
                return a.get(0) - b.get(0);
            } else {
                return b.get(1) - a.get(1);
            }
        });
        return result;

    }
}

