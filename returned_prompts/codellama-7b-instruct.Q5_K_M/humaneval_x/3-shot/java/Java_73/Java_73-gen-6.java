        int left = 0;
        int right = arr.size() - 1;

        while (left < right) {
            if (arr.get(left) == arr.get(right)) {
                left += 1;
                right -= 1;
            } else {
                int left_val = arr.get(left);
                int right_val = arr.get(right);
                if (Math.abs(left_val - right_val) == 1) {
                    left += 1;
                    right -= 1;
                } else {
                    return 2;
                }
            }
        }
        return 0;
    }
}

