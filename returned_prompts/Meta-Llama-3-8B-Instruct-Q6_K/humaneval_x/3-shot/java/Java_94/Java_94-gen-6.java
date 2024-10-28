        int max_prime = -1;
        for (int num : lst) {
            if (isPrime(num)) {
                if (num > max_prime) {
                    max_prime = num;
                }
            }
        }
        if (max_prime == -1) {
            return 0;
        }
        int sum = 0;
        while (max_prime > 0) {
            sum += max_prime % 10;
            max_prime /= 10;
        }
        return sum;
    }

    public boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        if (num == 2) {
            return true;
        }
        if (num % 2 == 0) {
            return false;
        }
        for (int i = 3; i * i <= num; i += 2) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

