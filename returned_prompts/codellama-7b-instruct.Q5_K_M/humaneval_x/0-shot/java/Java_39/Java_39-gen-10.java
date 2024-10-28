        int[] fibs = new int[n];
        fibs[0] = 1;
        fibs[1] = 2;
        for (int i = 2; i < n; i++) {
            fibs[i] = fibs[i - 1] + fibs[i - 2];
            for (int j = 2; j < Math.sqrt(fibs[i]); j++) {
                if (fibs[i] % j == 0) {
                    continue A;
                }
            }
        }
        return fibs[n - 1];
    }

    /**
    nextPrime returns the next prime number after n.
    >>> nextPrime(1)
    2
    >>> nextPrime(2)
    3
    >>> nextPrime(3)
    5
    >>> nextPrime(11)
    13
    >>> nextPrime(101)
    101
     */
    public int nextPrime(int n) {
        n++;
        while (true) {
            if (isPrime(n)) {
                return n;
            }
            n++;
        }
    }

    /**
    isPrime returns true if n is prime number, otherwise false.
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
     */
    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        if (n == 2 || n == 3) {
            return true;
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
