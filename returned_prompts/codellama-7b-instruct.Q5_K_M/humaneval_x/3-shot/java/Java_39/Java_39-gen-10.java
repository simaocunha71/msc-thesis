        int a = 1;
        int b = 2;
        for (int i = 0; i < n - 1; i++) {
            int c = a + b;
            if (isPrime(c)) {
                a = b;
                b = c;
            }
        }
        return b;
    }

    private boolean isPrime(int num) {
        if (num == 1 || num == 0) return false;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

