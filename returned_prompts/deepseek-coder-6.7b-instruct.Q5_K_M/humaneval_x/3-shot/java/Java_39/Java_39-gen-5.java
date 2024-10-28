        int fib1 = 2, fib2 = 3, fib3 = 5;
        int i = 2;
        if (n == 1) return fib1;
        if (n == 2) return fib2;
        if (n == 3) return fib3;
        while (i < n) {
            int temp = fib2;
            fib2 = fib3;
            fib3 = temp + fib3;
            if (isPrime(fib3)) i++;
        }
        return fib3;
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }
}

