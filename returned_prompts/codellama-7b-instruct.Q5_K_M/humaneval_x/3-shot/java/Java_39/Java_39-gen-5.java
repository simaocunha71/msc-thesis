        int a = 1;
        int b = 2;
        int c = 0;
        for (int i = 0; i < n - 1; i++) {
            c = a + b;
            a = b;
            b = c;
            if (isPrime(c)) {
                return c;
            }
        }
        return c;
    }

    private boolean isPrime(int num) {
        if (num == 1) {
            return false;
        }
        for (int i = 2; i < Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

