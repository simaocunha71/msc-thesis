        int count = 0;
        for (int num : nums) {
            if (Math.abs(num) > 10) {
                int digit = (int) (Math.abs(num) % 10);
                if (digit % 2 != 0) {
                    int first_digit = (int) ((Math.abs(num) / 10) % 10);
                    if (first_digit % 2 != 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}