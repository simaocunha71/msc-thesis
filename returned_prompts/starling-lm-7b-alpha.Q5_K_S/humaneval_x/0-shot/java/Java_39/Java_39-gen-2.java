        if (n == 1) {
            return 2;
        }
        if (n == 2) {
            return 3;
        }
        int i = 3;
        int fib = 2;
        int fib_prev = 3;
        while (true) {
            fib = fib + fib_prev;
            fib_prev = fib - fib_prev;
            if (fib_isPrime(fib)) {
                return fib;
            }
            if (i >= n) {
                break A;
            }
            i = i + 1;
        }
        return -1;
    }

    public boolean fib_isPrime(int fib) {
        if (fib < 2) {
            return false;
        }
        if (fib == 2) {
            return true;
        }
        if (fib % 2 == 0) {
            return false;
        }
        for (int i = 3; i * i <= fib; i += 2) {
            if (fib % i == 0) {
                return false;
            }
        }
        return true;
    }

}































































































































































































































