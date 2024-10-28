        int count = 0;
        int fib1 = 0;
        int fib2 = 1;
        int fib = 0;
        while (count < n) {
            fib = fib1 + fib2;
            fib1 = fib2;
            fib2 = fib;
            if (isPrime(fib)) {
                count++;
            }
        }
        return fib;
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

