        int fib1 = 0, fib2 = 1, fib3 = 1;
        int primeCounter = 0;

        while (primeCounter < n) {
            fib1 = fib2;
            fib2 = fib3;
            fib3 = fib1 + fib2;

            if (isPrime(fib2)) {
                primeCounter++;
            }
        }

        return fib2;
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

