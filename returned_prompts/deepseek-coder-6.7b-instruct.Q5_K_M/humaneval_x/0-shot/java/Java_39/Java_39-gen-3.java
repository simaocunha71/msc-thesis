        int a = 0, b = 1, c = 0;
        int count = 0;
        while (count < n) {
            c = a + b;
            a = b;
            b = c;
            if (isPrime(c)) {
                count++;
            }
        }
        return c;
    }

    private boolean isPrime(int n) {
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
}

The solution provides a function primeFib(int n) to find the n-th Fibonacci number that is also prime. This function uses a while loop to increment the Fibonacci sequence until it finds the n-th prime number. It uses another function isPrime(int n) to check if a number is prime. The function isPrime(int n) checks if a number is divisible by any number up to the square root of that number. If it is, then the number is not prime.

The function primeFib(int n) keeps track of the count of prime Fibonacci numbers it has found. When it finds a prime number, it increments the count. The loop continues until it has found n prime Fibonacci numbers. It then returns the last prime Fibonacci number it found.

The time complexity of the solution is O(n*sqrt(m)) where n is the input number and m is the n-th Fibonacci number. This is because for each Fibonacci number, it checks if it is prime which takes O(sqrt(m)) time. The space complexity of the solution is O(1) as it only uses a constant amount of space.

The solution may not be the most efficient for large inputs due to the time complexity, but it works for the given constraints and is simple and easy to understand.
*/

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.primeFib