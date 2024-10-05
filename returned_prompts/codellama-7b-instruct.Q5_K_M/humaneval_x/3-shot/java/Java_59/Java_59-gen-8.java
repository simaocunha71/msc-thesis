        for (int i = n / 2; i >= 2; i--) {
            if (n % i == 0 && isPrime(i)) {
                return i;
            }
        }
        return 1;
    }

    private boolean isPrime(int n) {
        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

