        int count = 0;
        for(List<Integer> row : grid) {
            for(int well : row) {
                if(well == 1) {
                    count++;
                }
            }
        }
        return count / capacity + (count % capacity > 0 ? 1 : 0);
    }
}

