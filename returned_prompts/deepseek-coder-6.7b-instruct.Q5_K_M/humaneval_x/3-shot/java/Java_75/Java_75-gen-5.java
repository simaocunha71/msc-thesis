        int primeFactorCount = 0;

        for (int i = 2; i <= a; i++) {
            while (a % i == 0) {
                primeFactorCount++;
                a /= i;
            }
        }
        return primeFactorCount == 3;
    }
}

