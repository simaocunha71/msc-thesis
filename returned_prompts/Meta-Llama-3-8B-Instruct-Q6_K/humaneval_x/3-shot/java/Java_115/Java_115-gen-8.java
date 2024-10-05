        int count = 0;
        for (List<Integer> row : grid) {
            for (int cell : row) {
                if (cell == 1) {
                    count += capacity;
                }
            }
        }
        return count;
    }
}

