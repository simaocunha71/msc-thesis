        int count = 0;
        for (List<Integer> row : grid) {
            for (int water : row) {
                count += water;
            }
        }
        return (count + capacity - 1) / capacity;
    }
}

