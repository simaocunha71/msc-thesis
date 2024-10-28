        List<Integer> result = new ArrayList<>(nums);
        Collections.sort(result, (a, b) -> {
            int as = sumDigits(a);
            int bs = sumDigits(b);
            if (as != bs) return Integer.compare(as, bs);
            return Integer.compare(a, b);
        });
        return result;
    }

    /**
    Sum all digits of given number.
    >>> sumDigits(123) == 6
    >>> sumDigits(0) == 0
    >>> sumDigits(-1) == -1
    */
    public int sumDigits(int number) {
        int result = 0;
        for (; number != 0; result += number % 10, number /= 10);
        return result;
    }
}

