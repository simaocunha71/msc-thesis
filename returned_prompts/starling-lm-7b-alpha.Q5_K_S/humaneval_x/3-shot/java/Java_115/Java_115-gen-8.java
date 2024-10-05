        int total_capacity = 0;
        int total_buckets = 0;
        int total_wells = 0;
        for (List<Integer> row : grid) {
            total_wells += row.size();
            total_capacity += row.size();
            total_buckets += Collections.frequency(row, 1);
        }

        return total_capacity / capacity * total_wells / capacity * total_buckets;
    }
}

