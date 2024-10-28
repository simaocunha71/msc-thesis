        int rows = grid.size();
        int cols = grid.get(0).size();
        int[][] buckets = new int[rows][cols];
        int[][] water = new int[rows][cols];

        // Initialize the buckets
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                buckets[i][j] = grid.get(i).get(j);
            }
        }

        // Initialize the water
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                water[i][j] = buckets[i][j];
            }
        }

        int count = 0;
        boolean done = false;

        while (!done) {
            done = true;

            for (int j = 0; j < cols; j++) {
                if (buckets[rows - 1][j] > 0) {
                    done = false;
                    int water_left = buckets[rows - 1][j];

                    // Move the water
                    for (int i = rows - 2; i >= 0; i--) {
                        int water_to_fill = Math.min(water_left, capacity);
                        buckets[i][j] = water_left - water_to_fill;
                        water[i][j] += water_to_fill;
                        water_left = water_left - water_to_fill;
                        if (water_left == 0) {
                            break;
                        }
                    }

                    // Check if the well is empty
                    if (water[0][j] > 0) {
                        count++;
                        done = false;
                    }

                    // Reset the buckets
                    for (int i = 0; i < rows; i++) {
                        buckets[i][j] = water[i][j];
                    }
                }
            }
        }

        return count;
   