        int[] a = new int[]{2, 3, 5, 13, 89, 337, 881, 1789, 4839, 12589, 31781, 63231, 127969, 286243, 574089, 1398269, 3191089, 6770489, 13468579};
        if (n <= 17) {
            return a[n - 1];
        }
        int[] fib = new int[n + 1];
        fib[0] = 0;
        fib[1] = 1;
        for (int i = 2; i <= n; i++) {
            fib[i] = fib[i - 1] + fib[i - 2];
        }
        int ret = 0;
        for (int i = 0; i < fib.length; i++) {
            if (isPrime(fib[i])) {
                ret = fib[i];
                break A;
            }
        }
        return ret;
    }

    /**
    isPrime returns true if n is prime, false otherwise.
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
    >>> isPrime(11)
    true
    >>> isPrime(12)
    false
    >>> isPrime(13)
    true
    >>> isPrime(14)
    false
    >>> isPrime(15)
    false
    >>> isPrime(16)
    false
    >>> isPrime(1