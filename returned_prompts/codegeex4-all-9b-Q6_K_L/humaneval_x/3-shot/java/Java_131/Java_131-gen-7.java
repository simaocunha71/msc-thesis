        int result = 1;
        int temp = n;

        while (temp > 0) {
            int digit = temp % 10;
            if (digit % 2 != 0) {
                result *= digit;
            }
            temp /= 10;
        }
        return result;
    }
}

