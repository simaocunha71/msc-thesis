        int max_index = -1;
        int max_value = Integer.MIN_VALUE;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > max_value) {
                max_index = i;
                max_value = arr.get(i);
            }
        }
        return max_index;
    }
}

