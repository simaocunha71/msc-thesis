        int a = 0;
        int b = 1;
        for (int i = 0; i < n; i++) {
            int c = a + b;
            if (isPrime(c)) {
                a = b;
                b = c;
            }
        }
        return a + b;
    }

    /**
    isPrime returns true if n is prime number.
    >>> isPrime(1)
    false
    >>> isPrime(2)
    true
    >>> isPrime(3)
    true
    >>> isPrime(4)
    false
    >>> isPrime(5)
    true
    >>> isPrime(6)
    false
    >>> isPrime(7)
    true
    >>> isPrime(8)
    false
    >>> isPrime(9)
    false
    >>> isPrime(10)
    false
     */
    public boolean isPrime(int n) {
        if (n == 1) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        for (int i = 2; i < Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
