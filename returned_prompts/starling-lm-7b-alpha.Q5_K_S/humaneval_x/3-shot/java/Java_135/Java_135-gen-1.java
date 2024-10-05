        int max_index = -1;
        for (int i = 0; i < arr.size(); i++) {
            int current = arr.get(i);
            if (i > 0 && current > arr.get(i - 1)) {
                if (current > max_index) {
                    max_index = current;
                } else {
                    return i - 1;
                }
            }
        }
        return max_index;
    }
}

