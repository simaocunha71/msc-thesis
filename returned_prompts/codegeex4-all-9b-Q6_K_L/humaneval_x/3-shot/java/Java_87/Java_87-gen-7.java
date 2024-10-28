        List<List<Integer>> result = new ArrayList<>();
        for (int row = 0; row < lst.size(); row++) {
            for (int col = lst.get(row).size() - 1; col >= 0; col--) {
                if (lst.get(row).get(col) == x) {
                    List<Integer> coordinate = new ArrayList<>();
                    coordinate.add(row);
                    coordinate.add(col);
                    result.add(coordinate);
                }
            }
        }
        return result;
    }
}

