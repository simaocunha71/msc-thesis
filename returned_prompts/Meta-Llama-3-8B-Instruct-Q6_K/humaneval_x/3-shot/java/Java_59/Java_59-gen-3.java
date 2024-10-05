        int max_prime = 1;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                int prime = i;
                while (n % prime == 0) {
                    max_prime = prime;
                    n /= prime;
                }
            }
        }
        return max_prime;
    }
}

