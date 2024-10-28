        int result = 1;
        boolean has_odd = false;

        while (n > 0) {
            int current_digit = n % 10;

            if (current_digit % 2 == 1) {
                result *= current_digit;
                has_odd = true;
            }

            n /= 10;
        }

        return has_odd ? result : 0;

    }
}

