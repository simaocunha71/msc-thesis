        int total = 0;
        for (List<Integer> row : grid) {
            for (int cell : row) {
                total += cell;
            }
        }
        return (int) Math.ceil((double) total / capacity);
    }
}

