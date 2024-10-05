        int max = 0;
        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                boolean isPrime = true;
                for (int j = 2; j * j <= i; j++) {
                    if (i % j == 0) {
                        isPrime = false;
                        break;
                    }
                }
                if (isPrime) {
                    max = i;
                }
            }
        }
        return max;
    }
}