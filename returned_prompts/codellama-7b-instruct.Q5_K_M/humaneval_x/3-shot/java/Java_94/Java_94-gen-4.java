        int largest_prime = -1;
        for (int i : lst) {
            if (i > largest_prime) {
                if (isPrime(i)) {
                    largest_prime = i;
                }
            }
        }
        return sumDigits(largest_prime);
    }

    private boolean isPrime(int n) {
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    private int sumDigits(int num) {
        int result = 0;
        while (num > 0) {
            result += num % 10;
            num /= 10;
        }
        return result;
    }
}

