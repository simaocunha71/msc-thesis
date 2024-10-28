        int a = 0, b = 1, c = 0;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }

    /**
    Return the index of the first element in the given array that is greater than the given value.
    If no such element exists, return the length of the array.
    >>> findFirstGreater(0, [1, 2, 3, 4, 5, 6])
    0
    >>> findFirstGreater(2, [1, 2, 3, 4, 5, 6])
    2
    >>> findFirstGreater(3, [1, 2, 3, 4, 5, 6])
    3
    >>> findFirstGreater(4, [1, 2, 3, 4, 5, 6])
    4
    >>> findFirstGreater(5, [1, 2, 3, 4, 5,