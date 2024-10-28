        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));
        int length = end - start;

        if (length < 2) {
            return "NO";
        }

        boolean[] primes = new boolean[length + 1];
        primes[0] = primes[1] = true;

        for (int i = 2; i * i <= length; i++) {
            if (!primes[i]) {
                for (int j = i * i; j <= length; j += i) {
                    primes[j] = true;
                }
            }
        }

        return primes[length] ? "YES" : "NO";
    }
}

