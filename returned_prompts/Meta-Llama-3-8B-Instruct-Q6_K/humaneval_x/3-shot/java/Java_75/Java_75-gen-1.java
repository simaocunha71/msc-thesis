        for (int i = 2; i <= Math.sqrt(a); i++) {
            if (isPrime(i)) {
                for (int j = i; j <= Math.sqrt(a / i); j++) {
                    if (isPrime(j) && a % (i * j) == 0) {
                        return true;
                    }
                }
            }
        }
        return false;

    }

    boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

