        int max = 0;
        for (int i : lst) {
            if (isPrime(i)) {
                if (i > max) {
                    max = i;
                }
            }
        }
        int sum = 0;
        while (max != 0) {
            sum += max % 10;
            max /= 10;
        }
        return sum;
    }

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

