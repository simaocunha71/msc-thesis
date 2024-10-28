Here is a possible solution in Java:

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
        if (num <= 1) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
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

Explanation:

- The `skjkasdkd` function iterates through the list `lst` and checks if each number is prime and greater than the current maximum prime (`maxPrime`). If it is, it updates `maxPrime`.
- The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if any of the numbers divide the number evenly.
- The `sumDigits` function calculates the sum of the digits of a number by repeatedly taking the last digit (`num % 10`) and adding it to the sum, then removing the last digit (`num /= 10`) until the number is 0.