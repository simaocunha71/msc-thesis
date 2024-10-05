        if (arr.size() == 0) return true;

        int largest = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > largest) {
                largest = arr.get(i);
            }
        }

        int shift_count = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) == largest) {
                shift_count += 1;
            }
        }

        if (shift_count == 0) return false;

        for (int i = 0; i < shift_count; i++) {
            arr.set(arr.size() - 1, arr.get(arr.size() - 2));
            arr.remove(arr.size() - 2);
        }
        return true;
    }
}

