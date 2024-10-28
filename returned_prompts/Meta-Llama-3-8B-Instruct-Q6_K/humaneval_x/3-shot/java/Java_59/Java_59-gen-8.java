        int max_prime = 1;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                int factor = i;
                while (n % factor == 0) {
                    n /= factor;
                    factor = n % factor == 0 ? i : factor;
                }
                max_prime = factor;
            }
        }
        return max_prime;
    }
}

