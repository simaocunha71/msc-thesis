        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            int min = Integer.MAX_VALUE;
            int row = 0;
            int col = 0;
            for (int j = 0; j < grid.size(); j++) {
                for (int h = 0; h < grid.get(0).size(); h++) {
                    if (grid.get(j).get(h) < min) {
                        min = grid.get(j).get(h);
                        row = j;
                        col = h;
                    }
                }
            }
            result.add(min);
            grid.get(row).set(col, Integer.MAX_VALUE);
        }
        return result;
    }
}

