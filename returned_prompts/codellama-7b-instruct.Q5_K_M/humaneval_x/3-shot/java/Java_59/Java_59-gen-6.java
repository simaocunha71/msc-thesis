        while (true) {
            if (isPrime(n)) {
                return n;
            }
            n -= 1;
        }
    }

    private boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }

        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }
}

