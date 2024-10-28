        int count = 0;
        for (int num : nums) {
            if (num > 10) {
                int first_digit = num / 10 % 10;
                int last_digit = num % 10;
                if (first_digit % 2 != 0 && last_digit % 2 != 0) {
                    count++;
                }
            }
        }
        return count;
    }
}

