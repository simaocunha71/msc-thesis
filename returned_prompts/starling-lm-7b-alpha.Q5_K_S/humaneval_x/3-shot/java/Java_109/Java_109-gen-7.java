        int max_index = 0;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) > arr.get(max_index)) {
                max_index = i;
            }
        }
        int current_index = max_index;
        while (current_index != 0) {
            int tmp = arr.get(current_index);
            arr.set(current_index, arr.get(0));
            arr.set(0, tmp);
            current_index -= 1;
        }
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) < arr.get(i - 1)) {
                return false;
            }
        }
        return true;
    }
}

