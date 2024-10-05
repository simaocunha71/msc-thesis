        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            List<Integer> row = lst.get(i);
            int rowSize = row.size();
            for (int j = 0; j < rowSize; j++) {
                if (row.get(j) == x) {
                    List<Integer> temp = new ArrayList<>();
                    temp.add(i);
                    temp.add(j);
                    result.add(temp);
                }
            }
        }
        result.sort(Comparator.comparingInt(o -> o.get(0)));
        result.forEach(l -> l.sort(Comparator.comparingInt(o -> -o.get(1))));
        return result;
    }
}
