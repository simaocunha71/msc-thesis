        int a = 0;
        int b = 1;
        int c = 0;
        int count = 1;

        while (count < n) {
            c = a + b;
            a = b;
            b = c;
            count += 1;
        }

        while (true) {
            if (isPrime(c)) return c;
            c += 1;
        }

    }

    public boolean isPrime(int n) {
        if (n < 2) return false;

        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }

        return true;
    }
}

