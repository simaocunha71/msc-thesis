    int N = sentence.length();

    List<Integer> primes = getPrimes(N);

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < N; i++) {
        int len = 0;
        while (i < N && len < primes.get(primes.size() - 1)) {
            sb.append(sentence.charAt(i++));
            len++;
        }

        if (len == primes.get(primes.size() - 1)) {
            primes.remove(primes.size() - 1);
        }
    }

    return sb.toString();
}

private List<Integer> getPrimes(int N) {
    boolean[] prime = new boolean[N + 1];
    Arrays.fill(prime, true);
    List<Integer> res = new ArrayList<>();
    for (int i = 2; i <= N; i++) {
        if (prime[i]) {
            res.add(i);
            for (int j = 2 * i; j <= N; j += i) {
                prime[j] = false;
            }
        }
    }
    return res;
}
}


























































































































































































































