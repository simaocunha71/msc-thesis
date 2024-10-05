        int rows = grid.size();
        int cols = grid.get(0).size();
        int totalWater = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                totalWater += grid.get(i).get(j);
            }
        }
        int count = totalWater / capacity;
        if (totalWater % capacity > 0) {
            count++;
        }
        return count;
    }
}

