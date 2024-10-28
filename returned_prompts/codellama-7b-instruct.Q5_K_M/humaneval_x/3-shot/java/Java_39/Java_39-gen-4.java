        int a = 0, b = 1;
        while (n > 0) {
            int t = a + b;
            a = b;
            b = t;
            if (isPrime(a)) n -= 1;
        }
        return a;
    }

    private boolean isPrime(int num) {
        if (num < 2) return false;
        if (num == 2) return true;

        for (int i = 2; i < num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

