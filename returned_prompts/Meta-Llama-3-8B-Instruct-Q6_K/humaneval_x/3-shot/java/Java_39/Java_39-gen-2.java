        int a = 0, b = 1;
        int count = 0;
        while (true) {
            int fib = a + b;
            a = b;
            b = fib;
            if (isPrime(fib)) {
                count++;
                if (count == n) return fib;
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

