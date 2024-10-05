        int n = grid.size();
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid.get(i).get(j) == 1) {
                    result.add(grid.get(i).get(j));
                    break;
                }
            }
        }

        for (int i = 0; i < k - 1; i++) {
            List<Integer> next = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                if (result.get(j) + 1 < n) {
                    next.add(result.get(j) + 1);
                } else {
                    next.add(result.get(j));
                }
            }
            result = next;
        }
        return result;
    }
}

