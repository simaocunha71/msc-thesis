        int result = 0;
        int total_water = 0;
        while (total_water > 0) {
            for (List<Integer> row : grid) {
                if (total_water == 0) break;
                int water = 0;
                for (int i = 0; i < row.size(); i++) {
                    if (water + row.get(i) <= capacity) {
                        water += row.get(i);
                    } else {
                        grid.get(result).set(i, grid.get(result).get(i) - capacity - water + row.get(i));
                        total_water -= capacity - water;
                        water = row.get(i);
                    }
                }
            }
            result += 1;
        }
        return result;
    }
}

