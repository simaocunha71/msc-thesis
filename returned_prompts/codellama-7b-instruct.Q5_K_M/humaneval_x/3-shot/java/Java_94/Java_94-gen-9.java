        int max_prime = 0;
        for (int i : lst) {
            if (i > max_prime && isPrime(i)) {
                max_prime = i;
            }
        }
        return sumDigits(max_prime);
    }

    private boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    private int sumDigits(int n) {
        int result = 0;
        while (n != 0) {
            result += n % 10;
            n /= 10;
        }
        return result;
    }
}

