        int maxPrime = 2;
        for (int i = 3; i * i <= n; i += 2) {
            while (n % i == 0) {
                n /= i;
                maxPrime = i;
            }
        }
        if (n > 2) {
            maxPrime = n;
        }
        return maxPrime;
    }
}