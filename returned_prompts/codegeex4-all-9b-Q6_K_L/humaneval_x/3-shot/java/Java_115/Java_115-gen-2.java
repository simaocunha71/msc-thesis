        int max_fill = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(i).size(); j++) {
                if (grid.get(i).get(j) == 1) {
                    max_fill += 1;
                    grid.get(i).set(j, 0);
                }
            }
        }
        return max_fill;
    }
}

