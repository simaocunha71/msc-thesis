        int totalWater = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(i).size(); j++) {
                if (grid.get(i).get(j) == 1) {
                    totalWater += 1;
                }
            }
        }
        return (int) Math.ceil(totalWater / (double) capacity);
    }
}

