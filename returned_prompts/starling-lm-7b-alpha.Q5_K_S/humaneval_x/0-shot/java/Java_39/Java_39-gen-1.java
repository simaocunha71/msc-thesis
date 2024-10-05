        if (n == 0) {
            return 2;
        }

        int x = 1;
        int y = 2;

        while (n > 1) {

            int tmp = x + y;
            int isPrime = true;

            for (int i = 2; i <= Math.sqrt(tmp); i++) {
                if (tmp % i == 0) {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime) {
                if (n == 1) {
                    return y;
                }
                n--;
                x = y;
                y = tmp;
                continue A;
            }

        }
        return -1;
    }

    /**
    isPrime returns true if n is a prime number, false otherwise.
    >>> isPrime(1)
    False
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
    >>> isPrime(11)
    True
    >>> isPrime(12)
    False
    >>> isPrime(13)
    True
    >>> isPrime(14)
    False
    >>> isPrime(15)
    False
    >>> isPrime(16)
    False
    >>> isPrime(17)
    True
    >>> isPrime(18)
    False
    >>> isPrime(19)
    True
    >>> isPrime(20)
    False
    >>> isPrime(21)
    False
    >>> isPrime(22)
    False
    >>> isPrime(23)
    True
    >>> isPrime(2