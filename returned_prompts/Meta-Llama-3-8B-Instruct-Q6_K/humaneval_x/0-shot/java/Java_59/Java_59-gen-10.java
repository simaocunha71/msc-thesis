        int i = 2, maxPrimeFactor = 0;
        while (i * i <= n) {
            if (n % i == 0) {
                maxPrimeFactor = i;
                while (n % i == 0) {
                    n /= i;
                }
            }
            i++;
        }
        if (n > 1) {
            maxPrimeFactor = n;
        }
        return maxPrimeFactor;
    }
}
