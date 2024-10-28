        int a = 2, b = 3, count = 1;
        while (count < n) {
            a = a + b;
            if (isPrime(a)) {
                b = a;
                count++;
            }
        }
        return a;
    }

    public boolean isPrime(int num) {
        if (num < 2) {
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

Solution class contains two methods:
1. `primeFib(int n)`: This method returns the nth number that is a Fibonacci number and it's also prime.
2. `isPrime(int num)`: This method checks if a given number is prime or not.

Note: The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. In this problem, we start with 2 and 3 as our initial Fibonacci numbers.

The `primeFib` method starts with `a = 2` and `b = 3`, and then iterates until it finds the `n`th prime Fibonacci number. In each iteration, it calculates the next Fibonacci number as `a = a + b`, and checks if it's prime using the `isPrime` method. If it's prime, it increments the count and updates `b` to be the new Fibonacci number. Finally, it returns the `n`th prime Fibonacci number.