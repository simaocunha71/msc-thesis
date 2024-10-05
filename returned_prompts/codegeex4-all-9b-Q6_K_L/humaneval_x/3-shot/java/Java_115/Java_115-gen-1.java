        int sum = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(i).size(); j++) {
                sum += grid.get(i).get(j);
            }
        }
        return sum / capacity;
    }
}