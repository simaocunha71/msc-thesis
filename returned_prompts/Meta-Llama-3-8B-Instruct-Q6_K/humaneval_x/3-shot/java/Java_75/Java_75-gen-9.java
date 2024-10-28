        for (int i = 2; i <= 100; i++) {
            for (int j = i + 1; j <= 100; j++) {
                for (int k = j + 1; k <= 100; k++) {
                    if (i * j * k == a) {
                        if (isPrime(i) && isPrime(j) && isPrime(k)) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }

    private boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}

