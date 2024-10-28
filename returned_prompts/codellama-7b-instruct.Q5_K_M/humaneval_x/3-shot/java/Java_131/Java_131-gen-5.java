        int result = 0;
        int current_digit = 0;
        while (n > 0) {
            current_digit = n % 10;
            if (current_digit % 2 != 0) {
                result *= current_digit;
            }
            n /= 10;
        }
        return result;
    }
}

