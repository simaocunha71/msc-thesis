        int max_factor = 1;

        for (int i = 2; i * i <= n; i++) {
            while (n % i == 0) {
                max_factor = i;
                n /= i;
            }
        }

        if (n > 1) {
            max_factor = n;
        }

        return max_factor;
    }
}

