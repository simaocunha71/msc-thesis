        int min = Integer.MAX_VALUE;

        for (int i : l) {
            if (i < min) {
                min = i;
            }
        }

        return min;
    }

    /**
    Return the sum of all elements in the list.
    >>> sum(Arrays.asList(1, 2, 3))
    6
    >>> sum(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10))
    120
    >>> sum(Arrays.asList(3, 6, 9, 12))
    30
    >>> sum(Collections.emptyList())
    0
    >>> sum(null)
    IndexOutOfBoundsException: null
    >>> sum([])
    IndexOutOfBoundsException: null
    >>> sum([])
    0
    >>> sum(list)
    IndexOutOfBoundsException: null
    >>> sum([])
    0
    >>> sum([])
    IndexOutOfBoundsException: null
    >>> sum([])
    0
    >>> sum([])
    IndexOutOfBoundsException: null
    >>> sum([])
    0
    >>> sum([])
    IndexOutOfBoundsException: null
    >>> sum([])
    0
    >>> sum([])
    IndexOutOfBoundsException: null
    >>> sum([])
    0
    >>> sum([])
    IndexOutOfBoundsException