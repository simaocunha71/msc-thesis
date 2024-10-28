        int result = 0;
        int rows = grid.size();
        int columns = grid.get(0).size();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (grid.get(i).get(j) == 1) {
                    result += 1;
                    grid.get(i).set(j, 0);
                }
            }
        }
        return result;
    }
}

