        int a = 1;
        int b = 2;
        int c = a + b;
        for (int i = 1; i < n; i++) {
            if (isPrime(c)) {
                return c;
            }
            a = b;
            b = c;
            c = a + b;
        }
        return c;
    }

    /**
     * isPrime:
     *   return true if a number is prime.
     *   >>> isPrime(2)
     *   true
     *   >>> isPrime(3)
     *   true
     *   >>> isPrime(4)
     *   false
     *   >>> isPrime(5)
     *   true
     *   >>> isPrime(6)
     *   false
     *   >>> isPrime(7)
     *   true
     *   >>> isPrime(8)
     *   false
     *   >>> isPrime(9)
     *   false
     *   >>> isPrime(10)
     *   false
     *   >>> isPrime(11)
     *   true
     */
    public boolean isPrime(int n) {
        for (int i = 2; i < n / 2; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
