        int result = 0;
        Queue<Integer> queue = new LinkedList<>();
        int total_water = 0;
        while (!queue.isEmpty() || total_water > 0) {
            while (!queue.isEmpty()) {
                int well_index = queue.poll();
                if (grid.get(well_index).get(result % grid.get(well_index).size()) == 1) {
                    grid.get(well_index).set(result % grid.get(well_index).size(), 0);
                    total_water -= 1;
                }
            }
            for (int i = 0; i < grid.size(); i++) {
                if (grid.get(i).get(result % grid.get(i).size()) == 1) {
                    queue.add(i);
                    total_water += 1;
                }
            }
            result += 1;
        }
        return result - 1;
    }
}

