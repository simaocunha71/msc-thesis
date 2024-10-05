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
        for (int i = 2; i < num; i++) {
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

In this solution, the `skjkasdkd` method iterates through the list of integers. For each integer, it checks if it is a prime number using the `isPrime` method. If it is a prime number and greater than the current maximum prime number (`maxPrime`), it updates `maxPrime`. 

After finding the largest prime number, the method calculates the sum of its digits using the `sumDigits` method and returns it. 

The `isPrime` method checks if a number is a prime number by iterating from 2 to the number and checking if the number is divisible by any of these values. 

The `sumDigits` method calculates the sum of the digits of a number by repeatedly taking the remainder of the number when divided by 10 (this gives the last digit), adding it to the sum, and then dividing the number by 10 (this removes the last digit).