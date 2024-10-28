        int maxPrime = 0;
        for (int i : lst) {
            if (isPrime(i) && i > maxPrime) {
                maxPrime = i;
            }
        }
        int sumOfDigits = 0;
        while (maxPrime > 0) {
            sumOfDigits += maxPrime % 10;
            maxPrime /= 10;
        }
        return sumOfDigits;
    }

    public boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        int i = 3;
        while (i * i <= n) {
            if (n % i == 0) return false;
            i += 2;
        }
        return true;
    }
}

