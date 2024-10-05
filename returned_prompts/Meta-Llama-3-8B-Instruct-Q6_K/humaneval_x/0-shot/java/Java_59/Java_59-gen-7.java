        int largestFactor = 0;
        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                int temp = n / i;
                if (isPrime(temp)) {
                    largestFactor = temp;
                }
            }
        }
        return largestFactor;
    }

    // helper function to check if a number is prime
    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

