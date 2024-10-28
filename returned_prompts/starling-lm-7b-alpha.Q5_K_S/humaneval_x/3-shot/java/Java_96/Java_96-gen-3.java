        List<Integer> result = new ArrayList<>();
        if (n < 2) return result;
        boolean[] primes = new boolean[n + 1];
        Arrays.fill(primes, true);
        primes[0] = false;
        primes[1] = false;
        for (int i = 2; i * i <= n; i++) {
            if (primes[i]) {
                for (int j = i * i; j <= n; j += i) {
                    primes[j] = false;
                }
            }
        }
        for (int i = 0; i < primes.length; i++) {
            if (primes[i]) result.add(i);
        }
        return result;
    }
}

