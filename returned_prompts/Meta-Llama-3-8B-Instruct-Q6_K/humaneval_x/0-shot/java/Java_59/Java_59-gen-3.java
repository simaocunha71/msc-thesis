        int largestFactor = 1;
        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                largestFactor = i;
                while (n % i == 0) {
                    n = n / i;
                }
            }
        }
        return largestFactor;
    }
}

