        int largestPrime = 0;

        for (int i : lst) {
            if (isPrime(i) && i > largestPrime) largestPrime = i;
        }
        return largestPrime;
    }

    private boolean isPrime(int n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

