        if (n == 1) return 2;
        if (n == 2) return 3;

        int a = 2;
        int b = 3;
        int result = 0;

        while (n > 3) {
            int c = a + b;
            if (isPrime(c)) {
                result = c;
            }
            a = b;
            b = c;
            n--;
        }
        return result;
    }

    public boolean isPrime(int candidate) {
        for (int i = 2; i * i <= candidate; i++) {
            if (candidate % i == 0) return false;
        }
        return true;
    }
}

