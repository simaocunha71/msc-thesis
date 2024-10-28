Here is a Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int skjkasdkd(List<Integer> lst) {
        int maxPrime = 0;
        for (int num : lst) {
            if (isPrime(num) && num > maxPrime) {
                maxPrime = num;
            }
        }
        return sumDigits(maxPrime);
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

    private int sumDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
```

In the `skjkasdkd` method, we iterate through the list of integers. If the number is prime and greater than the current maximum prime, we update the maximum prime. After iterating through all the numbers, we return the sum of the digits of the maximum prime.

The `isPrime` method checks if a number is prime or not. It returns `true` if the number is prime, and `false` otherwise.

The `sumDigits` method calculates the sum of the digits of a number. It returns the sum.