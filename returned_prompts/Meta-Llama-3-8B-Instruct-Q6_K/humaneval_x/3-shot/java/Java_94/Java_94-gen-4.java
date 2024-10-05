        int maxPrime = 0;
        for (int i : lst) {
            if (isPrime(i) && i > maxPrime) {
                maxPrime = i;
            }
        }
        return sumOfDigits(maxPrime);
    }

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public int sumOfDigits(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}