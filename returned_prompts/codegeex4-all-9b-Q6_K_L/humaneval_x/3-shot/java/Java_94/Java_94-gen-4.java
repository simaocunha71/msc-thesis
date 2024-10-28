        int max_prime = -1;

        for (int num : lst) {
            if (isPrime(num) && num > max_prime) {
                max_prime = num;
            }
        }

        int sum = 0;
        while (max_prime > 0) {
            sum += max_prime % 10;
            max_prime /= 10;
        }
        return sum;
    }

    private boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

