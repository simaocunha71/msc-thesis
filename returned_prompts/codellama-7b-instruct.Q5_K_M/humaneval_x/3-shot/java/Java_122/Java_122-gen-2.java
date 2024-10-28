        int result = 0;
        int n = arr.size();
        int max_index = Math.min(k, n);
        int min_index = 0;

        while (min_index < max_index) {
            int current_sum = arr.get(min_index) + arr.get(max_index);
            if (current_sum < 100) {
                result += current_sum;
                min_index += 1;
            } else {
                max_index -= 1;
            }
        }

        return result;
    }
}

