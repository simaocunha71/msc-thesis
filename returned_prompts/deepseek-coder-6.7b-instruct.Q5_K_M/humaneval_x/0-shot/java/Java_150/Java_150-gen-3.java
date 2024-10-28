        if (isPrime(n)) {
            return x;
        } else {
            return y;
        }
    }

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i < Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

Explanation:
The function isPrime checks whether a given number is prime or not by iterating from 2 to the square root of the number and checking if the number is divisible by any of these numbers. If the number is divisible by any of these numbers, it's not prime and the function returns false. If the number is not divisible by any of these numbers, it's prime and the function returns true.

The function xOrY takes three integers as input. If the first integer (n) is prime, it returns the value of the second integer (x). If n is not prime, it returns the value of the third integer (y).

In the provided examples, the numbers 7, 15, and 12 are prime numbers while the numbers 34 and 8 are not. So, for the first example, the function returns 34 because 7 is a prime number, and for the second example, the function returns 5 because 15 is not a prime number.

Note: The Math.sqrt(n) is used to optimize the function by reducing the number of iterations. This is because a larger factor of the number must be a multiple of a smaller factor that has already been checked.
*/

// End of code

// Start of test cases

import java.util.*;
import java.lang.*;

class TestCases {
    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();

        // Test case 1
        System.out.println("Expected: 34, Actual: " + solution.xOrY(7, 34, 12));

        // Test case 2
        System.out.println("Expected: 5, Actual