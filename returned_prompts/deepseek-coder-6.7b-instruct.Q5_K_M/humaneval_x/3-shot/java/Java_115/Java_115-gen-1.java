        int total_wells = 0;
        for (List<Integer> row : grid) total_wells += sum(row);

        return (total_wells + capacity - 1) / capacity;
    }
}

