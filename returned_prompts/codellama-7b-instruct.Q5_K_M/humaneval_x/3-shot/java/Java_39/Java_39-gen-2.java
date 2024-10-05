        int a = 0;
        int b = 1;
        int c = 0;

        for (int i = 0; i < n - 1; i++) {
            c = a + b;
            a = b;
            b = c;
        }

        if (isPrime(c)) {
            return c;
        } else {
            return -1;
        }
    }

    private boolean isPrime(int n) {
        if (n == 1 || n == 2) {
            return true;
        } else if (n % 2 == 0) {
            return false;
        }

        int sqrtN = (int) Math.sqrt(n);

        for (int i = 3; i <= sqrtN; i += 2) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }
}

