        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = lst.get(i).size() - 1; j >= 0; j--) {
                if (lst.get(i).get(j) == x) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }
        Collections.sort(result, (a, b) -> a.get(0) - b.get(0));
        Collections.sort(result, (a, b) -> b.get(1) - a.get(1));
        return result;
    }
}

