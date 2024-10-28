        List<Integer> primes = new ArrayList<>();
        boolean[] notPrime = new boolean[n + 1];
        for (int i = 2; i <= n; i++) {
            if (!notPrime[i]) {
                primes.add(i);
                for (int j = i + i; j <= n; j += i) {
                    notPrime[j] = true;
                }
            }
        }
        return primes;
    }
}

