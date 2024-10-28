        int a = 0, b = 1, count = 0;
        while (true) {
            int fib = a + b;
            a = b;
            b = fib;
            if (isPrime(b) && ++count == n) {
                return b;
            }
        }
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

