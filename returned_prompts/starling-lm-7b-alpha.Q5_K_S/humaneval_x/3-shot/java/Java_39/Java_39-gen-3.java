        int fib = 0;
        int a = 0;
        int b = 1;
        while (fib < n) {
            fib = a + b;
            if (isPrime(fib)) return fib;
            a = b;
            b = fib;
        }
        return -1;
    }

    private boolean isPrime(int num) {
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

