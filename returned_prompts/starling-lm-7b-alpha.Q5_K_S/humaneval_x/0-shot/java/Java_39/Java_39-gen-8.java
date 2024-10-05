        for (int i = 1; i < n; i++) {
            int fib = fib(i);
            if (isPrime(fib)) {
                return fib;
            }
        }
        return -1;
    }

    /**
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(7)
    13
    >>> fib(8)
    21
    >>> fib(9)
    34
    >>> fib(10)
    55
    >>> fib(11)
    89
    >>> fib(12)
    144
    >>> fib(13)
    233
     */
    private int fib(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        return fib(n - 1) + fib(n - 2);
    }

    /**
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
    >>> isPrime(17)
    true
    >>> isPrime(18)
    false
    >>> isPrime(19)
    true
    >>> isPr