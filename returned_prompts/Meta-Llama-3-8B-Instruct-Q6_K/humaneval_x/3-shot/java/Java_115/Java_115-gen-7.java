        int count = 0;
        for (List<Integer> row : grid) {
            int fill = 0;
            for (int well : row) {
                if (well == 1) {
                    fill++;
                }
            }
            count += fill / capacity;
            fill %= capacity;
        }
        return count;
    }
}

