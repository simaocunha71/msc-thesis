        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(0).size(); j++) {
                if (grid.get(i).get(j) == 1) {
                    return grid.get(i);
                }
            }
        }

        return null;
    }
}
