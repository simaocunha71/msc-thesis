        List<Integer> result = new ArrayList<>();
        List<Integer> temp = new ArrayList<>(nums);
        Collections.sort(temp, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int sum_a = sumOfDigits(a);
                int sum_b = sumOfDigits(b);
                if (sum_a != sum_b) return sum_a - sum_b;
                return Integer.compare(a, b);
            }
        });
        return temp;
    }

    /**
    Returns sum of all digits of a number.
    >>> sumOfDigits(123)
    6
    >>> sumOfDigits(0)
    0
    >>> sumOfDigits(-123)
    -6
     */
    public int sumOfDigits(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}

