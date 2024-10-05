        for (int i = 2; i <= a; i++) {
            if (isPrime(i) && a % i == 0) {
                for (int j = i + 1; j <= a / i; j++) {
                    if (isPrime(j) && a % j == 0) {
                        for (int k = j + 1; k <= a / (i * j); k++) {
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

