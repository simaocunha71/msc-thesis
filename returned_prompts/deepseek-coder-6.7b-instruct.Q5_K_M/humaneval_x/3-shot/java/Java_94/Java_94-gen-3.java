        int max_prime = -1;
        for (int num : lst) {
            if (isPrime(num) && num > max_prime) {
                max_prime = num;
            }
        }
        return sumOfDigits(max_prime);
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    private int sumOfDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

