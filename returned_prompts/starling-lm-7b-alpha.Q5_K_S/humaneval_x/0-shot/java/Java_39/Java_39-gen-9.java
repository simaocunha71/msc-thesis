        if (n == 0 || n == 1) {
            return 0;
        }

        int fib = 1;
        int count = 0;
        int prevFib = 1;

        while (count < n) {
            fib = fib + prevFib;
            prevFib = fib - prevFib;

            if (fib % 2 != 0) {
                if (isPrime(fib)) {
                    return fib;
                }
            }

            count += 1;
        }

        return -1;
    }

    private boolean isPrime(int n) {
        if (n == 2 || n == 3) {
            return true;
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}










































































































































































































































