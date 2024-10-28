        if (n == 1) return 2;
        if (n == 2) return 3;

        int a = 0;
        int b = 1;

        for (int i = 1; i < n; i++) {
            int c = a + b;
            a = b;
            b = c;
            if (isPrime(c)) {
                return c;
            }
        }
        return 0;
    }

    boolean isPrime(int n) {
        if (n == 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

