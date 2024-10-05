        int max = 1;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                while (n % i == 0) {
                    n /= i;
                }
                max = i;
            }
        }
        if (n > 1) {
            max = n;
        }
        return max;
    }
}

