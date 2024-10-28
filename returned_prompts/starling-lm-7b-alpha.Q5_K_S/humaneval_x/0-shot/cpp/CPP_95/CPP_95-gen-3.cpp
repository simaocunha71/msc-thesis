        int result = 0;
        int total_water = 0;

        while (total_water > 0) {
            total_water = 0;
            for (int i = 0; i < grid.size(); i++) {
                total_water += grid.get(i).get(result % capacity);
            }
            result += total_water / capacity;
        }
        return result;
    }
}

