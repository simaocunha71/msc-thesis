        int rows = grid.size();
        int cols = grid.get(0).size();
        int bucket_times = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid.get(i).get(j) == 1) {
                    bucket_times += capacity;
                }
            }
        }
        return bucket_times;
    }
}

