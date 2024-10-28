        int n = grid.size();
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid.get(i).get(j) == 1) {
                    result.add(grid.get(i).get(j));
                }
            }
        }
        return result;
    }
}

