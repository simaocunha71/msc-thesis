    if (isPrime(n)) {
        return x;
    } else {
        return y;
    }
}

// Function to check if a number is prime
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