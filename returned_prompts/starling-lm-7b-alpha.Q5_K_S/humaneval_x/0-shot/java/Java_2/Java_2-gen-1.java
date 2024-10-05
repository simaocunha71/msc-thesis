    while (number > 0) {
        number /= 10;
        if (number >= 1 && number < 2) {
            break A;
        }
    }
    return number;
    }

    /**
    Given a number, find the next number after it in the Fibonacci sequence.

    >>> nextFibonacci(2)
    3
    >>> nextFibonacci(3)
    5
    >>> nextFibonacci(5)
    8
    >>> nextFibonacci(10)
    34
    >>> nextFibonacci(21)
    109
    >>> nextFibonacci(99)
    218922995834555169025
    >>> nextFibonacci(100)
    218922995834555169026
    >>> nextFibonacci(Integer.MAX_VALUE)
    12200160415121876738

    The first two numbers in the Fibonacci sequence are 0 and 1.
    Every other number is the sum of the two preceding ones,
    so the Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

    Complexity: O(log n)
    */
    public long nextFibonacci(long number) {
        if (number <= 0) {
            return 0;
        }
        if (number == 1) {
            return 1;
        }
        long p = 1, q = 0, r = 1;
        while (number > 0) {
            long t = p;
            p = q + r;
            q = t;
            r = p - q;
            number--;
        }
        return q;
    }

    /**
    Given an array of integers, return a new array of integers such that each
    integer in the input array is squared, and then sorted