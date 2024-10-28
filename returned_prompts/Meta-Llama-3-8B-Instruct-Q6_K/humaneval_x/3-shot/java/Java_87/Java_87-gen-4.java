        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    List<Integer> pair = new ArrayList<>();
                    pair.add(i);
                    pair.add(j);
                    result.add(pair);
                }
            }
        }
        Collections.sort(result, (a, b) -> {
            if (a.get(0).equals(b.get(0))) {
                return b.get(1) - a.get(1);
            } else {
                return a.get(0) - b.get(0);
            }
        });
        return result;
    }
}

