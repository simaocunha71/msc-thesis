        int result = 0;
        for (List<Integer> row : grid) {
            for (int bucket : row) {
                if (bucket == 1) {
                    result += 1;
                    if (result % capacity == 0) {
                        result = 0;
                    }
                }
            }
        }
        return result;
    }
}

