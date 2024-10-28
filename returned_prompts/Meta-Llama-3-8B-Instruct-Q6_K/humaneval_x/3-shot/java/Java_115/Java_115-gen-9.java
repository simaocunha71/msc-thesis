        int total_water = 0;
        for (List<Integer> row : grid) {
            total_water += row.stream().mapToInt(i -> i).sum();
        }
        return (total_water + capacity - 1) / capacity;
    }
}

