        for (int i = n; i > 0; i--) {
            if (n % i == 0 && isPrime(i)) {
                return i;
            }
        }
        return 0;
    }

    private boolean isPrime(int n) {
        if (n == 1 || n == 2) return true;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

