        if (p == 1) {
            return 0;
        }
        int result = 1;
        while (n > 0) {
            if (n % 2 == 1) {
                result = (int) ((result * (long) result) % p);
            }
            n /= 2;
            result = (int) ((result * (long) result) % p);
        }
        return result;
    }


    /**
    >>> binsearch(1, 5, 3)
    3
    >>> binsearch(1, 5, 4)
    4
    >>> binsearch(1, 5, 0)
    1
    >>> binsearch(1, 5, 2)
    2
    >>> binsearch(1, 5, 6)
    5
    >>> binsearch(1, 5, 7)
    5
    >>> binsearch(1, 5, 8)
    5
    >>> binsearch(1, 5, 9)
    5
    >>> binsearch(1, 5, 10)
    5
    >>> binsearch(1, 5, 11)
    5
    >>> binsearch(1, 5, 12)
    5
    >>> binsearch(1, 5, 13)
    5
    >>> binsearch(1, 5, 14)
    5
    >>> binsearch(1, 5, 15)
    5
    >>> binsearch(1, 5, 16)
    5
    >>> binsearch(1, 5, 17)
    5
    >>> binsearch(1, 5, 18)
    5
    >>> binsearch(1, 5, 19)
    5
    >>> binsearch(1, 5, 20)
    5
    >>> binsearch(1, 5, 21)
    5
    >>> binsearch(1, 5, 22)
    5
    >>> binsearch(1, 5, 23)
    5
    >>> binsearch(1, 5,