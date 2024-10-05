        int max_prime = 1;

        for (int i = 2; i * i <= n; i++) {
            while (n % i == 0) {
                max_prime = i;
                n /= i;
            }
        }

        if (n > 1) max_prime = n;

        return max_prime;
    }
}

