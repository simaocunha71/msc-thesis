Here is a Java solution for the problem:

```java
import java.util.*;

class Solution {
    public boolean isMultiplyPrime(int a) {
        if (a < 2) {
            return false;
        }
        
        int count = 0;
        for (int i = 2; i <= a; i++) {
            if (a % i == 0) {
                if (!isPrime(i)) {
                    return false;
                }
                count++;
                a /= i;
                i--;
            }
        }
        
        return count == 3;
    }

    private boolean isPrime(int num) {
        if (num < 2) {
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

The `isMultiplyPrime` method first checks if the number is less than 2, if it is, then it returns false since 1 is not a prime number.

Next, it initializes a counter to 0, which will be used to keep track of the number of prime factors.

The method then enters a loop that starts from 2 and goes up to the given number. If the given number is divisible by the current number, it checks if the current number is a prime number. If it is not, then it returns false since the given number is not a multiplication of 3 prime numbers.

If the current number is a prime number, then it increments the counter and divides the given number by the current number. It also decrements the current number by 1 so that the loop can continue from the correct number.

After the loop, the method checks if the counter is equal to 3, if it is, then it returns true since the given number is a multiplication of 3 prime numbers. Otherwise, it returns false.