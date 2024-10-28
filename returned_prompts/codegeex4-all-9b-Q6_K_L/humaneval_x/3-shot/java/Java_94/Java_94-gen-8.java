        int max_prime = Integer.MIN_VALUE;
        for (int num : lst) {
            if (isPrime(num)) {
                max_prime = Math.max(max_prime, num);
            }
        }
        return sumDigits(max_prime);
    }

    public boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public int sumDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

