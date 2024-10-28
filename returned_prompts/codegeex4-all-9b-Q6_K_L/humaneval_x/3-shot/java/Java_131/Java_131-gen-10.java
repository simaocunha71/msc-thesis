        int result = 0;
        int temp = n;
        while (temp > 0) {
            int digit = temp % 10;
            if (digit % 2 == 1) {
                result *= digit;
            }
            temp /= 10;
        }
        return result;
    }
}

