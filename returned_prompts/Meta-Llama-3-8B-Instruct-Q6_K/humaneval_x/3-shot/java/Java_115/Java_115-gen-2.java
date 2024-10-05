        int count = 0;
        for (List<Integer> row : grid) {
            int total = 0;
            for (int cell : row) {
                total += cell;
            }
            count += total / capacity;
        }
        return count;
    }
}

