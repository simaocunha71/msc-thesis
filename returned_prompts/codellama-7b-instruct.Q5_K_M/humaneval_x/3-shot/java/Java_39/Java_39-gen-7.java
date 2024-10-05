        int a = 0;
        int b = 1;

        for (int i = 0; i < n; i++) {
            int c = a + b;
            if (isPrime(c)) {
                a = b;
                b = c;
            } else {
                a = c;
            }
        }
        return b;
    }

    private boolean isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++) {
            if (x % i == 0) return false;
        }
        return true;
    }
}

