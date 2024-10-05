        List<List<Integer>> result = new ArrayList<>();
        int row = -1;
        int col = -1;

        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    row = i;
                    col = j;
                    List<Integer> current = new ArrayList<>();
                    current.add(row);
                    current.add(col);
                    result.add(current);
                }
            }
        }

        result.sort(Comparator.comparing(o -> o.get(0)));
        result.sort(Comparator.comparing(o -> -o.get(1)));

        return result;

    }
}

