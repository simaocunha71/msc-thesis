        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            List<Integer> row = lst.get(i);
            int column = row.indexOf(x);
            if (column > -1) {
                result.add(Arrays.asList(i, column));
            }
        }
        Collections.sort(result, (l1, l2) -> l1.get(0) - l2.get(0));
        Collections.sort(result.get(0), (l1, l2) -> l2.get(1) - l1.get(1));
        return result;
    }
}

