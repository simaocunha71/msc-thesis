        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                int last_digit = num % 10;
                int first_digit = (int) Math.floor(num / 10) % 10;
                if (last_digit % 2 != 0 && first_digit % 2 != 0) {
                    count++;
                }
            }
        }
        return count;
    }
}