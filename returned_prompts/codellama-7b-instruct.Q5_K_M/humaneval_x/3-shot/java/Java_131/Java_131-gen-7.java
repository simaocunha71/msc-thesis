        int result = 1;
        for (int i = 0; i < n; i++) {
            int digit = n % 10;
            if (digit % 2 != 0) result *= digit;
            n /= 10;
        }
        return result;
    }
}

