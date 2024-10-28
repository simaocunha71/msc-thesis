        int sum = 0;
        int max_value = 0;
        int max_index = 0;

        for (int i = 0; i < k; i++) {
            if (arr.get(i) > max_value) {
                max_value = arr.get(i);
                max_index = i;
            }
        }

        if (max_value > 99) {
            arr.set(max_index, 1);
            sum = 1;
        } else if (max_value > 9) {
            sum = max_value % 10 + max_value / 10;
            arr.set(max_index, 0);
        } else {
            sum = max_value;
            arr.set(max_index, 0);
        }

        for (int i = k; i < arr.size(); i++) {
            sum += arr.get(i);
        }
        return sum;
    }
}

