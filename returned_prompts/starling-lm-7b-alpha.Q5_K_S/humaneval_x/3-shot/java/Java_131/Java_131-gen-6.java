        int product = 1;
        boolean all_even = true;

        for (int i = 0; i < String.valueOf(n).length(); i++) {
            int digit = n % 10;
            n /= 10;

            if (digit % 2 == 1) {
                product *= digit;
                all_even = false;
            }
        }

        return all_even ? 0 : product;
    }
}

