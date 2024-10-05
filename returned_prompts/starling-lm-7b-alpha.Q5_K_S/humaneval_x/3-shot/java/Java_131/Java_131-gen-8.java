        int result = 1;
        while (n != 0) {
            int digit = n % 10;
            if (digit % 2 == 1) {
                result *= digit;
            }
            n /= 10;
        }
        return result;
    }
}

