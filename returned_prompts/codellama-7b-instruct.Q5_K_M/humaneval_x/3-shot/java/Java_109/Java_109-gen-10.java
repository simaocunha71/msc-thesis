        if (arr.isEmpty()) return true;
        int current_max = arr.get(0);
        int current_max_index = 0;

        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) > current_max) {
                current_max = arr.get(i);
                current_max_index = i;
            }
        }

        if (current_max_index == arr.size() - 1) return true;

        for (int i = 0; i < arr.size(); i++) {
            if (i == current_max_index) {
                arr.set(i, arr.get(arr.size() - 1));
                arr.set(arr.size() - 1, current_max);
            }
        }

        for (int i = 0; i < arr.size() - 1; i++) {
            if (arr.get(i) > arr.get(i + 1)) return false;
        }

        return false;
    }
}

