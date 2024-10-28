        for (int i = 2; i <= 100; i++) {
            for (int j = i; j <= 100; j++) {
                for (int k = j; k <= 100; k++) {
                    if (i * j * k == a) {
                        return isPrime(i) && isPrime(j) && isPrime(k);
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

