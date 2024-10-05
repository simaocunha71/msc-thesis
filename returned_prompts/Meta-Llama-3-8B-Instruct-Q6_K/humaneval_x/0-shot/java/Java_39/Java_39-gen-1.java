        int a = 0, b = 1;
        int count = 0;
        while (true) {
            a = a + b;
            b = a - b;
            if (isPrime(a)) {
                count++;
                if (count == n) {
                    return a;
                }
            }
        }
    }

    public boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

Explanation:
The function `primeFib` generates Fibonacci numbers and checks if they are prime using the helper function `isPrime`. It stops when it finds the n-th prime Fibonacci number. The `isPrime` function checks if a number is prime by dividing it by all numbers up to its square root.

The time complexity of this solution is O(n*sqrt(n)) because for each Fibonacci number, it checks if it's prime by iterating up to its square root. The space complexity is O(1) because it only uses a constant amount of space.