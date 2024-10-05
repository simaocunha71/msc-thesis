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

        // sort coordinates by row, then by column
        result.sort(Comparator.comparing(e -> e.get(0)));
        result.sort(Comparator.comparing(e -> e.get(1), Comparator.reverseOrder()));
        return result;
    }
}

