        for (int i = n / 2; i > 1; i--) {
            if (n % i == 0 && isPrime(i)) return i;
        }
        return 1;
    }

    public boolean isPrime(int n) {
        if (n == 2 || n == 3) return true;
        if (n < 2 || n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }
}

