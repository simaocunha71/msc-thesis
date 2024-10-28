        int result = 0;
        int largest_prime = 0;
        for (int number : lst) {
            if (isPrime(number)) {
                result += sumDigits(number);
                largest_prime = Math.max(largest_prime, number);
            }
        }
        return result;
    }

    int sumDigits(int n) {
        int sum = 0;
        while (n != 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;

        if (n % 2 == 0 || n % 3 == 0) return false;

        for (int i = 5; i * i <= n; i = i + 6)
            if (n % i == 0 || n % (i + 2) == 0)
                return false;

        return true;
    }
}

