public boolean isPrime(int n) {
    // n is less than 2, so it's not prime
    if (n < 2) {
        return false;
    }
    // n is 2, so it's prime
    if (n == 2) {
        return true;
    }
    // n is even, so it's not prime
    if (n % 2 == 0) {
        return false;
    }
    // Check for factors up to the square root of n
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    // If no factors were found, n is prime
    return true;
}