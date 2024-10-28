        int result = 0;
        for (int i : nums) {
            int first_digit = (i / 10000000) % 10;
            int last_digit = i % 10;

            if (first_digit % 2 != 0 && last_digit % 2 != 0 && i > 10) {
                result += 1;
            }
        }
        return result;
    }
}

