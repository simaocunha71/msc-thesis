        List<List<Integer>> result = new ArrayList<>();

        for (int row = 0; row < lst.size(); row++) {
            for (int col = 0; col < lst.get(row).size(); col++) {
                if (lst.get(row).get(col) == x) {
                    List<Integer> coordinate = new ArrayList<>();
                    coordinate.add(row);
                    coordinate.add(col);
                    result.add(coordinate);
                }
            }
        }

        result.sort(Comparator.comparing((List<Integer> p) -> p.get(0)).thenComparing((List<Integer> p) -> p.get(1), Comparator.reverseOrder()));

        return result;
    }
}

