        return l.stream().filter(x -> x > 0).collect(Collectors.toList());
    }

    /**
    Return only negative numbers in the list.
    >>> getNegative(Arrays.asList(-1, 2, -4, 5, 6))
    [-1, -4, -6]
    >>> getNegative(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10))
    [-5, -3, -3, -10]
     */
    public List<Integer> getNegative(List<Integer> l) {

B:
        return l.stream().filter(x -> x < 0).collect(Collectors.toList());
    }

    /**
    Return only numbers that are multiples of 3.
    >>> getMultiplesOf3(Arrays.asList(-1, 2, -4, 5, 6, 18))
    [6, 18]
    >>> getMultiplesOf3(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10, -12))
    [3, -3, 9, -12]
     */
    public List<Integer> getMultiplesOf3(List<Integer> l) {

C:
        return l.stream().filter(x -> x % 3 == 0).collect(Collectors.toList());
    }

    /**
    Return only numbers that are multiples of 2.
    >>> getMultiplesOf2(Arrays.asList(-1, 2, -4, 5, 6, 18))
    [2, 6, 18]
    >>> getMultiplesOf2(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10, -12))
    [2, 3, 9, -10,