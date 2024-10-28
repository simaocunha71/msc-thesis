        for (int i = n; i > 2; i--) {
            if (n % i == 0 && isPrime(i)) return i;
        }
        return 2;
    }

    private boolean isPrime(int n) {
        if (n <= 1) return false;

        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

