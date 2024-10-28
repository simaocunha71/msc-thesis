        int max = 0;
        for (int i : lst) {
            if (i > max && isPrime(i))
                max = i;
        }
        return sumDigits(max);
    }

    private static boolean isPrime(int n) {
        // Iterate from 2 to n-1
        for (int i = 2; i < n; i++) {
            if (n % i == 0)
                return false;
        }
        return true;
    }

    private static int sumDigits(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}

