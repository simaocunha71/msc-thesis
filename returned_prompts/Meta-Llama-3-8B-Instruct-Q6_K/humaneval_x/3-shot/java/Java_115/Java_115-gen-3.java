        int count = 0;
        for (List<Integer> row : grid) {
            int water = 0;
            for (int cell : row) {
                water += cell;
            }
            count += water / capacity + (water % capacity > 0 ? 1 : 0);
        }
        return count;
    }
}

