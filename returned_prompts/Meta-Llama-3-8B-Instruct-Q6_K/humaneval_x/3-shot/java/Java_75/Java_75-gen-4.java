        for (int i = 2; i <= 100; i++) {
            if (isPrime(i) && a % i == 0) {
                for (int j = i; j <= 100; j++) {
                    if (isPrime(j) && a % j == 0) {
                        for (int k = j; k <= 100; k++) {
                            if (isPrime(k) && a % k == 0) {
                                return true;
                            }
                        }
                    }
                }
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

