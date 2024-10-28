
The first method hasCloseElements is correct.
The second method separateParenGroups is correct.
The third method truncateNumber has a bug. The correct code is:
public double truncateNumber(double number) {
    return number - (int) number;
}

The fourth method primeFib has a bug. The correct code is:
public int primeFib(int n) {
    List<Integer> fib = new ArrayList<>();
    fib.add(0);
    fib.add(1);

    for (int i = 2; i < n + 2; i++) {
        int new_fib = fib.get(i - 1) + fib.get(i - 2);
        fib.add(new_fib);
    }

    for (int i = 1; i < fib.size(); i++) {
        if (isPrime(fib.get(i))) {
            n -= 1;
            if (n == 0) {
                return fib.get(i);
            }
        }
    }

    return -1;
}

The fifth method isPrime is correct.