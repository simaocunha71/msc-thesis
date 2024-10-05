        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(i).size(); j++) {
                if (grid.get(i).get(j) == 1) {
                    return grid.get(i);
                }
            }
        }
        return grid.get(0);
    }
}
