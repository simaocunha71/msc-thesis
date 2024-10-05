Here is the Java code that solves the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int skjkasdkd(List<Integer> lst) {
        int maxPrime = Integer.MIN_VALUE;
        for (int num : lst) {
            if (isPrime(num) && num > maxPrime) {
                maxPrime = num;
            }
        }
        return sumOfDigits(maxPrime);
    }

    private boolean isPrime(int num) {
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

    private int sumOfDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
```

This code first iterates through the list of integers and checks if each number is prime and greater than the current maximum prime number. If a number is prime and greater than the current maximum prime number, it updates the maximum prime number. After finding the maximum prime number, it calculates the sum of its digits and returns the result. The `isPrime` method checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these numbers. The `sumOfDigits` method calculates the sum of the digits of a number by repeatedly taking the remainder when the number is divided by 10 and adding it to the sum, then dividing the number by 10.