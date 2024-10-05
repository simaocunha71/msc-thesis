        int result = 0;
        int total_capacity = capacity * grid.size();
        while (total_capacity > 0) {
            boolean found_water = false;
            for (int i = 0; i < grid.size(); i++) {
                int water_in_well = grid.get(i).get(grid.get(i).size() - 1);
                if (water_in_well == 1) {
                    found_water = true;
                    grid.get(i).remove(grid.get(i).size() - 1);
                    total_capacity -= capacity;
                    result += 1;
                }
            }
            if (!found_water) {
                return result;
            }
        }
        return result;
    }
}

