        for (int i = n / 2; i >= 2; i--) {
            if (n % i == 0 && isPrime(i)) return i;
        }
        return 2;
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

