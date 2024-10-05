        int max_factor = 1;
        for (int i = 2; i * i <= n; i++) {
            while (n % i == 0) {
                max_factor = i;
                n /= i;
            }
        }
        return max_factor;
    }
}

