        for (int i = n; i > 1; i--) {
            if (isPrime(i)) {
                return i;
            }
        }
        return 1;
    }

    public boolean isPrime(int n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

