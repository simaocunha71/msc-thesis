        int largest = -1;

        // Divide n by 2 until n becomes odd
        while (n % 2 == 0) {
            largest = 2;
            n >>= 1;
        }

        // Find odd factors of n
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                largest = i;
                n = n / i;
            }
        }

        // This condition is to handle the case when n is a prime number
        // greater than 2
        if (n > 2)
            largest = n;

        return largest;
    }
}

