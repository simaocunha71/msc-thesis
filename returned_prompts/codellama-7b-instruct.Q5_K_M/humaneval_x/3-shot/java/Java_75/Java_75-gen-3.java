        if (a < 100) return false;
        if (a == 100) return true;

        for (int i = 2; i < 10; i++) {
            if (a % i == 0) {
                if (isPrime(i)) {
                    if (isPrime(a / i)) return true;
                }
            }
        }
        return false;
    }

    public boolean isPrime(int a) {
        for (int i = 2; i < a; i++) {
            if (a % i == 0) return false;
        }
        return true;
    }
}

