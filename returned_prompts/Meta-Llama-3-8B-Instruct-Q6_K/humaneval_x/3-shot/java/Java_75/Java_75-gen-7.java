        for (int i = 2; i <= Math.sqrt(a); i++) {
            if (isPrime(i)) {
                int b = a / i;
                if (isPrime(b)) {
                    int c = a / (i * b);
                    if (isPrime(c)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private boolean isPrime(int a) {
        for (int i = 2; i <= Math.sqrt(a); i++) {
            if (a % i == 0) {
                return false;
            }
        }
        return true;
    }
}

