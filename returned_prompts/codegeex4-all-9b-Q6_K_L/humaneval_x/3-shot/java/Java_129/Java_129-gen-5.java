        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(0).size(); j++) {
                result.add(Arrays.asList(grid.get(i).get(j), i, j));
            }
        }

        Collections.sort(result, new Comparator<List<Integer>>() {
            @Override
            public int compare(List<Integer> o1, List<Integer> o2) {
                if (o1.get(0) > o2.get(0)) {
                    return 1;
                } else if (o1.get(0) < o2.get(0)) {
                    return -1;
                } else {
                    return 0;
                }
            }
        });

        List<Integer> min_path = new ArrayList<>();

        for (int i = 0; i < k; i++) {
            min_path.add(result.get(i).get(0));
        }

        return min_path;
    }
}

