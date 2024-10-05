        int result = 0;
        int wells_count = grid.size();
        int wells_length = grid.get(0).size();

        for (int i = 0; i < wells_length; i++) {
            int current_well_capacity = 0;
            for (List<Integer> well: grid) {
                if (well.get(i) == 1) current_well_capacity += 1;
            }
            if (current_well_capacity == 0) continue;

            while (current_well_capacity > 0) {
                int filled_wells = 0;
                for (int j = 0; j < wells_count; j++) {
                    if (grid.get(j).get(i) == 1 && current_well_capacity > 0) {
                        grid.get(j).set(i, 0);
                        current_well_capacity -= 1;
                        filled_wells += 1;
                    }
                }
                if (filled_wells == 0) break;
                result += 1;
            }
        }
        return result;
    }
}

