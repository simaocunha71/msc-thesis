        int even = 0;
        int odd = 0;

        while (num > 0) {
            int last_digit = num % 10;
            if (last_digit % 2 == 0) {
                even += 1;
            } else {
                odd += 1;
            }
            num /= 10;
        }
        return List.of(even, odd);
    }
}

