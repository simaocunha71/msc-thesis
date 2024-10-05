        return l.stream().filter(x -> x > 0).collect(Collectors.toList());
    }

    /**
    Return only numbers in the list that are not divisible by 3.
    >>> getNotDivisibleBy3(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    [1, 2, 4, 5, 7, 8]
    >>> getNotDivisibleBy3(Arrays.asList(1, 3, 5, 7, 9))
    [1, 5, 7]
     */
    public List<Integer> getNotDivisibleBy3(List<Integer> l) {
        return l.stream().filter(x -> x % 3 != 0).collect(Collectors.toList());
    }

    /**
    Return only numbers in the list that are not divisible by 3, and not divisible by 5.
    >>> getNotDivisibleBy3and5(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    [1, 2, 4, 5, 7, 8]
    >>> getNotDivisibleBy3and5(Arrays.asList(1, 3, 5, 7, 9))
    [1, 5, 7]
     */
    public List<Integer> getNotDivisibleBy3and5(List<Integer> l) {
        return l.stream().filter(x -> x % 3 != 0 && x % 5 != 0).collect(Collectors.toList());
    }

    /**
    Return only numbers in the list that are not divisible by 3, and not divisible by 5, and not divisible by 7.
    >>> getNotDivisibleBy3and5and7(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    [1, 