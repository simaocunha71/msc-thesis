        List<Integer> result = new ArrayList<>();
        boolean[] is_prime = new boolean[n + 1];
        Arrays.fill(is_prime, true);
        for (int i = 2; i * i <= n; i++) {
            if (is_prime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    is_prime[j] = false;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            if (is_prime[i + 1]) result.add(i + 1);
        }
        return result;
    }
}

