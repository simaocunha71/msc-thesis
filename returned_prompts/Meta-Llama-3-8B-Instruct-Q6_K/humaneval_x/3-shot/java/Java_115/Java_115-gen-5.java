        int totalWater = 0;
        for (List<Integer> row : grid) {
            for (int water : row) {
                totalWater += water;
            }
        }
        return (int) Math.ceil((double) totalWater / capacity);
    }
}