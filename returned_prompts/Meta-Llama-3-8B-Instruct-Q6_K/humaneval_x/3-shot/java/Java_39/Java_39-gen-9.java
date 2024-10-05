        int a = 0, b = 1, fib = 0, count = 0;
        while (count < n) {
            fib = a + b;
            a = b;
            b = fib;
            if (isPrime(fib)) {
                count++;
            }
        }
        return fib;
    }

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

