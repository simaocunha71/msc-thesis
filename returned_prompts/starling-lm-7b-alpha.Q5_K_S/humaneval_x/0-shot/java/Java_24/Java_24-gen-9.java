        for (int i = n / 2; i > 0; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return 1;
    }

    /**
    >>> isPrime(7)
    true
    >>> isPrime(10)
    false
    */
    public boolean isPrime(int n) {
        if (n == 2) {
            return true;
        }
        if (n == 3) {
            return true;
        }
        if (n < 2 || n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        int i = 5;
        while (i * i <= n) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
            i += 6;
        }
        return true;
    }
}

















































































































































































































































































