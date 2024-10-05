        int max_index = 0;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) > arr.get(i - 1)) {
                max_index = i;
            }
        }
        return max_index;
    }
}

