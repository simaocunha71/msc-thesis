        int result = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(i).size(); j++) {
                if (grid.get(i).get(j) == 1) {
                    grid.get(i).set(j, 0);
                    result += 1;
                    while (result % capacity != 0) {
                        for (int k = 0; k < grid.size(); k++) {
                            for (int l = 0; l < grid.get(k).size(); l++) {
                                if (grid.get(k).get(l) == 1) {
                                    grid.get(k).set(l, 0);
                                    result += 1;
                                    break;
                                }
                            }
                        }
                    }
                }
            }
        }
        return result / capacity;
    }
}

