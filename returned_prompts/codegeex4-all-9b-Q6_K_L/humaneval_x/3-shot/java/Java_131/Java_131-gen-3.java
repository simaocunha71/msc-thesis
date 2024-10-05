        int result = 1;
        boolean hasOdd = false;
        while (n > 0) {
            int digit = n % 10;
            if (digit % 2 == 1) {
                result *= digit;
                hasOdd = true;
            }
            n /= 10;
        }
        return hasOdd ? result : 0;
    }
}

