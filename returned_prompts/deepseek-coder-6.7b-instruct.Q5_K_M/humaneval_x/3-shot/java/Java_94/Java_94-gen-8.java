        int maxPrime = -1;
        for (int i : lst) {
            if (isPrime(i) && i > maxPrime) {
                maxPrime = i;
            }
        }
        return sumDigits(maxPrime);
    }

    private boolean isPrime(int num) {
        if (num < 2) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    private int sumDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

