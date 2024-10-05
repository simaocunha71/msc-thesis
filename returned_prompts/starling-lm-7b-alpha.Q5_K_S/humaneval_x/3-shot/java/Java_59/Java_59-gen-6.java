        Set<Integer> primes = getPrimesUpTo(n);
        for (int prime : primes) {
            while (n % prime == 0) {
                n /= prime;
            }
        }
        return n;
    }

    private Set<Integer> getPrimesUpTo(int limit) {
        boolean[] prime_set = new boolean[limit + 1];
        for (int i = 2; i < prime_set.length; i++) {
            prime_set[i] = true;
        }
        for (int i = 2; i < prime_set.length; i++) {
            if (prime_set[i]) {
                for (int j = i + i; j < prime_set.length; j += i) {
                    prime_set[j] = false;
                }
            }
        }
        Set<Integer> primes = new HashSet<>();
        for (int i = 2; i < prime_set.length; i++) {
            if (prime_set[i]) {
                primes.add(i);
            }
        }
        return primes;
    }
}

