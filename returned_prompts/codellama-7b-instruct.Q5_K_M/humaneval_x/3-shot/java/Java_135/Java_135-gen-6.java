        int previous_max_index = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > arr.get(i - 1)) {
                previous_max_index = i - 1;
            }
        }
        return previous_max_index;
    }
}

