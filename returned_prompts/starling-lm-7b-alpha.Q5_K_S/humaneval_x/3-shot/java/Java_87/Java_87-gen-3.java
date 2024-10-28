        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            List<Integer> row = lst.get(i);
            int j = 0;
            for (; j < row.size(); j++) {
                if (row.get(j) == x) {
                    result.add(Arrays.asList(i, j));
                    break;
                } else if (row.get(j) > x) {
                    break;
                }
            }
        }
        Collections.sort(result, (a, b) -> Integer.compare(a.get(0), b.get(0)));
        Collections.sort(result.get(0), (a, b) -> Integer.compare(b, a));
        return result;
    }
}

