        int a = 1, b = 1;
        int count = 0;

        while (true) {
            if (isPrime(b)) {
                count++;
                if (count == n) return b;
            }
            a = a + b;
            b = a - b;
        }
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

