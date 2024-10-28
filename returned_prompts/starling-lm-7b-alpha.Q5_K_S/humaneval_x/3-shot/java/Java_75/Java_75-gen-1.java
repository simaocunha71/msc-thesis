        Set<Integer> primes = new HashSet<>();
        for (int i = 2; i < 100; i++) {
            if (isPrime(i)) {
                primes.add(i);
            }
        }
        for (Integer prime : primes) {
            if (a % prime == 0) {
                a = a / prime;
            } else {
                return false;
            }
        }
        return a == 1;

    }

    private boolean isPrime(int number) {
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}

