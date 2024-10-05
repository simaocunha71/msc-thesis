        int max_divisor = -1;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                max_divisor = i;
            }
        }
        return max_divisor;
    }
}

