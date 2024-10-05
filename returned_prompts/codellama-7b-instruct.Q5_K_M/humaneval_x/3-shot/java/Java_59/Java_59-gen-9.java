        for (int i = n / 2; i > 1; i--) {
            if (n % i == 0 && isPrime(i)) return i;
        }
        return 1;
    }

    private boolean isPrime(int n) {
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

