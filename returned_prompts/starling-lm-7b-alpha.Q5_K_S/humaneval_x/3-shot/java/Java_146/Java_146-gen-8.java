        int result = 0;
        for (int num : nums) {
            int first_digit = (num / 10) % 10;
            int last_digit = num % 10;

            if (first_digit % 2 == 1 && last_digit % 2 == 1 && num > 10) {
                result += 1;
            }
        }
        return result;
    }
}


```