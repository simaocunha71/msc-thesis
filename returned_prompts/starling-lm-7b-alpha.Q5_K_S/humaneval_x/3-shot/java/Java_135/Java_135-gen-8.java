        int largest_index = arr.size() - 1;
        for (int i = arr.size() - 2; i >= 0; i--) {
            if (arr.get(i) > arr.get(i + 1)) {
                while (arr.get(i) > arr.get(largest_index)) {
                    largest_index -= 1;
                }
                if (largest_index <= i) return i;
                else arr.set(largest_index, arr.get(largest_index) + 1);
            }
        }
        return largest_index;
    }
}

