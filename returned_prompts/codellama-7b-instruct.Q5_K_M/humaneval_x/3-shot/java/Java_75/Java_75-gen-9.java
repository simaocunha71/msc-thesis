        if (a < 100) return false;

        int[] primes = new int[100];
        int count = 0;
        for (int i = 2; i < 100; i++) {
            if (isPrime(i)) {
                primes[count++] = i;
            }
        }

        for (int i = 0; i < count; i++) {
            for (int j = i + 1; j < count; j++) {
                for (int k = j + 1; k < count; k++) {
                    if (a == primes[i] * primes[j] * primes[k]) return true;
                }
            }
        }

        return false;
    }

    private boolean isPrime(int number) {
        if (number == 2) return true;
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}

