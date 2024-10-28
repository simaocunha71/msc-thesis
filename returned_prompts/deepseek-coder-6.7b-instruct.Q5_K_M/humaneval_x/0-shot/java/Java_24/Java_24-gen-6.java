        int largestDivisor = 1;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                if (n / i == i) {
                    largestDivisor = i;
                } else {
                    largestDivisor = n / i;
                }
            }
        }
        return largestDivisor;
    }
}

This program finds the largest divisor of a number n by iterating from 2 to the square root of n (since a larger factor of n must be a multiple of a smaller factor that has already been checked). It checks if n is evenly divisible by each number in the range, and if it is, it sets that number as the largest divisor. If not, it sets the quotient of n divided by the current number as the largest divisor. If no divisor other than 1 is found, the function returns 1.

This program uses a for loop and if statement to find the largest divisor of a number n, and it returns the largest divisor as the result.

The time complexity of this program is O(sqrt(n)), and the space complexity is O(1), because it only uses a constant amount of space to store the largest divisor and the loop variable.

The function is correct and does what the docstring says it should do, but it's not optimized for large inputs. The function could be optimized by checking for divisors in descending order, which would stop as soon as a divisor is found. This would reduce the number of iterations in the worst case.
    */
}

//src/main/java/com/example/demo/services/impl/LargestDivisorService.java
package com.example.demo.services.impl;

import com.example.demo.services.LargestDivisorServiceInterface;
import org.springframework.stereotype.Service;

@Service
public class LargestDivisorService implements LargestDivisorServiceInterface {

    @Override
    public int largestDivisor(int n) {
        int largestDivisor = 1;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0)