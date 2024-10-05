        int result = 0;
        for (Integer num : nums) {
            if (num > 10 && num % 2 == 1) {
                int first_digit = num / 10;
                int last_digit = num % 10;
                if (first_digit % 2 == 1 && last_digit % 2 == 1) {
                    result += 1;
                }
            }
        }
        return result;
    }
}

