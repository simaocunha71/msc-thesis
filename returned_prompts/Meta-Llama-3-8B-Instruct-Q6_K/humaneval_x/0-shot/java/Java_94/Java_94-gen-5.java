Here is a Java solution to find the largest prime number in the list and return the sum of its digits:

```java
import java.util.*;

public class Solution {
    public int skjkasdkd(List<Integer> lst) {
        int maxPrime = 0;
        for (int num : lst) {
            if (isPrime(num) && num > maxPrime) {
                maxPrime = num;
            }
        }
        return sumOfDigits(maxPrime);
    }

    public boolean isPrime(int num) {
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

    public int sumOfDigits(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}
```

This solution iterates through the list to find the largest prime number. It uses a helper function `isPrime` to check if a number is prime, and another helper function `sumOfDigits` to calculate the sum of the digits of a number. The main function `skjkasdkd` returns the sum of the digits of the largest prime number.