    // Check if the number is prime
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

// Example usage:
public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.xOrY(7, 34, 12)); // Output: 34
    System.out.println(solution.xOrY(15, 8, 5)); // Output: 5
}

This solution first checks if the number 'n' is prime by calling the 'isPrime' function. If 'n' is prime, it returns 'x', otherwise it returns 'y'. The 'isPrime' function checks if 'n' is less than or equal to 1 (in which case it's not prime), or if 'n' is divisible by any number from 2 to the square root of 'n' (in which case it's not prime). If 'n' passes these checks, it's considered prime and the function returns 'true'. The 'main' function demonstrates the usage of the 'xOrY' function with two examples.