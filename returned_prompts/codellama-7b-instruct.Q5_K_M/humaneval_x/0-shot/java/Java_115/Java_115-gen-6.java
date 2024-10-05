        for (int i = 0; i < grid.size(); i++) {
            int total = 0;
            for (int j = 0; j < grid.get(i).size(); j++) {
                if (grid.get(i).get(j) == 1) {
                    total += 1;
                }
            }
            if (total > capacity) {
                return -1;
            }
        }
        int total_wells = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(i).size(); j++) {
                if (grid.get(i).get(j) == 1) {
                    total_wells += 1;
                }
            }
        }
        int total_buckets = (grid.size() * grid.get(0).size()) / total_wells;
        int max = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(i).size(); j++) {
                if (grid.get(i).get(j) == 1) {
                    max += 1;
                }
            }
        }
        return total_wells * total_buckets / max;
    }
}
















