        int a = 1;
        int b = 1;
        int c = 0;
        int result = 0;

        for (int i = 0; i < n; i++) {
            c = a + b;
            a = b;
            b = c;
            if (c > 1 && isPrime(c)) {
                result = c;
            }
        }
        return result;
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;

        if (n % 2 == 0 || n % 3 == 0) return false;

        for (int i = 5; i * i <= n; i = i + 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}

