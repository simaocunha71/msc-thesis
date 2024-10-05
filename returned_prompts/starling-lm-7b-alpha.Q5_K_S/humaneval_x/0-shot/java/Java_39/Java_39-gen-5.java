        int prev = 0;
        int current = 1;
        int next = 1;
        int cnt = 2;
        while (cnt < n) {
            next = prev + current;
            prev = current;
            current = next;
            if (isPrime(next)) {
                cnt++;
                if (cnt == n) {
                    return next;
                }
            }
        }
        return -1;
    }

    /**
    isPrime checks if n is prime. It works in O(sqrt(n)) time.
    >>> isPrime(2)
    True
    >>> isPrime(3)
    True
    >>> isPrime(4)
    False
    >>> isPrime(5)
    True
    >>> isPrime(6)
    False
    >>> isPrime(7)
    True
    >>> isPrime(8)
    False
    >>> isPrime(9)
    False
    >>> isPrime(10)
    False
    >>> isPrime(21)
    False
    >>> isPrime(22)
    False
    >>> isPrime(23)
    True
    >>> isPrime(24)
    False
    >>> isPrime(25)
    False
    >>> isPrime(26)
    False
    >>> isPrime(27)
    False
    >>> isPrime(28)
    False
    >>> isPrime(29)
    True
    >>> isPrime(30)
    False
    >>> isPrime(31)
    True
    >>> isPrime(32)
    False
    >>> isPrime(33)
    False
    >>> isPrime(34)
    False
    >>> isPrime(35)
    False
    >>> isPrime(36)
    False
    >>> isPrime(37)
    True
    >>> isPrime(38)
    False
    >>> isPrime(39)
    False
    >>> isPrime(40)
    False
    >>> isPrime