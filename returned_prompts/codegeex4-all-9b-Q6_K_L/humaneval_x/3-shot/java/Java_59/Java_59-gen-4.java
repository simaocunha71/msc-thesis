        int max = -1;

        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                max = i;
                while (n % i == 0) {
                    n /= i;
                }
            }
        }

        return max;
    }
}

