        int max_prime_factor = 1;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                while (n % i == 0) {
                    n /= i;
                }
                max_prime_factor = i;
            }
        }
        return max_prime_factor;
    }
}

