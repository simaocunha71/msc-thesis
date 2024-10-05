        if (arr.size() == 0) return true;

        int max_index = -1;
        int max_val = Integer.MIN_VALUE;

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > max_val) {
                max_val = arr.get(i);
                max_index = i;
            }
        }

        if (max_val > 1) return false;
        if (max_val == 1) {
            if (max_index == 0) return false;
            return true;
        }

        int min_val = Integer.MAX_VALUE;
        int min_index = -1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < min_val) {
                min_val = arr.get(i);
                min_index = i;
            }
        }

        if (min_val < -1) return false;
        if (min_val == -1) {
            if (max_index == arr.size() - 1) return false;
            return true;
        }

        if (min_index != max_index) {
            Collections.swap(arr, min_index, max_index);
            return true;
        }

        return false;
    }
}

