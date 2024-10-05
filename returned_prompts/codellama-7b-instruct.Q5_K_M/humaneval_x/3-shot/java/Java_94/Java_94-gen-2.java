        int max_prime = 0;
        for (int i : lst) {
            if (isPrime(i) && i > max_prime) max_prime = i;
        }
        return sumDigits(max_prime);
    }

    private boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    private int sumDigits(int n) {
        if (n == 0) return 0;
        return n % 10 + sumDigits(n / 10);
    }
}

