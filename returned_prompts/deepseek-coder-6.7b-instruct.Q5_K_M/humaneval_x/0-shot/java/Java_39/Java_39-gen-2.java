        int i = 0, j = 1, count = 0, fib = 0;
        while (count < n) {
            fib = i + j;
            i = j;
            j = fib;
            if (isPrime(fib)) {
                count++;
            }
        }
        return fib;
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

Explanation:

- This solution works by generating Fibonacci numbers and checking if each one is prime. If it is, we increment a counter. When the counter reaches the input parameter n, we return that Fibonacci number as the n-th prime Fibonacci number.
- The isPrime method is a standard method for checking if a number is prime. It works by iterating from 2 up to the square root of the number, and checking if the number is divisible by any of these values. If it is, the number is not prime and the method returns false. If it is not divisible by any of these values, the number is prime and the method returns true.
- The primeFib method works by initializing two variables i and j to the first two Fibonacci numbers. It then enters a loop that continues until it has found the n-th prime Fibonacci number. In each iteration of the loop, it calculates the next Fibonacci number by adding i and j. It then shifts i and j to the next two Fibonacci numbers. If the new Fibonacci number is prime, it increments a counter. When the counter reaches n, the loop ends and the method returns the last prime Fibonacci number it found.
*/

//Time Complexity: O(n*sqrt(m)) where n is the input number and m is the Fibonacci number.
//Space Complexity: O(1) as we are not using any extra space that scales with the input size.

//