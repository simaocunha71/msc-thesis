        int result = 1;
        boolean all_even = true;

        while (n > 0) {
            int digit = n % 10;

            if (digit % 2 == 1) {
                result *= digit;
                all_even = false;
            }

            n /= 10;
        }

        return all_even ? 0 : result;
    }
}

