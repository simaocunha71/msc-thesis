        for (int i = 2; i <= 100; i++) {
            if (isPrime(i) && isPrime(a / i) && a % i == 0) {
                return true;
            }
        }
        return false;
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

