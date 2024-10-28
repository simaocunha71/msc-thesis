        // Check if the number is prime
        if (isPrime(n)) {
            return x; // if the number is prime, return x
        } else {
            return y; // if the number is not prime, return y
        }
    }

    // Method to check if a number is prime
    public boolean isPrime(int n) {
        // Corner cases
        if (n <= 1) {
            return false;
        }

        // Check from 2 to sqrt(n)
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return true;
    }
}
