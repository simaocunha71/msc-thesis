        int result = 0;
        for (int i = 0; i < nums.size(); i++) {
            int num = Math.abs(nums.get(i));
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

