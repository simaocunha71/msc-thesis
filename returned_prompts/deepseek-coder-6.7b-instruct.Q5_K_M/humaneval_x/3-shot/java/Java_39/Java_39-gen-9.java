        int count = 0;
        int fib1 = 1, fib2 = 1;
        int fibNext = 0;

        while (count < n) {
            fibNext = fib1 + fib2;
            fib1 = fib2;
            fib2 = fibNext;

            if (isPrime(fib2)) {
                count++;
            }
        }

        return fib2;
    }

    private boolean isPrime(int n) {
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

