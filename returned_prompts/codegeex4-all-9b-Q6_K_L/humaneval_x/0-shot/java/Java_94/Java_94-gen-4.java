Here is a way to solve the problem:

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
        if (maxPrime == 0) {
            return 0;
        }
        String digits = Integer.toString(maxPrime);
        int sum = 0;
        for (char digit : digits.toCharArray()) {
            sum += Character.getNumericValue(digit);
        }
        return sum;
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
}
```

Explanation:
The `skjkasdkd` function iterates over the list of integers and checks if each number is prime. If it is, it checks if it is larger than the current maximum prime number. If it is, it updates the maximum prime number. 

After iterating over the list, it checks if a prime number was found. If not, it returns 0. Otherwise, it converts the maximum prime number to a string and iterates over its digits. It adds each digit to a sum and returns the sum at the end. 

The `isPrime` function checks if a number is prime by iterating over all numbers from 2 to the square root of the number. If the number is divisible by any of these numbers, it is not prime. If it is not divisible by any of these numbers, it is prime.