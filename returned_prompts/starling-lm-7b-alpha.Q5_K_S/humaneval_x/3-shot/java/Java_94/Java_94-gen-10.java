        int max = 0;
        for (int i : lst) {
            if (isPrime(i)) {
                max = i;
            }
        }
        return sumOfDigits(max);
    }

    private boolean isPrime(int n) {
        if (n == 2) return true;
        if (n < 2 || n % 2 == 0) return false;
        double d = Math.sqrt(n);
        for (int i = 3; i <= d; i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    private int sumOfDigits(int number) {
        int sum = 0;
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }
}

