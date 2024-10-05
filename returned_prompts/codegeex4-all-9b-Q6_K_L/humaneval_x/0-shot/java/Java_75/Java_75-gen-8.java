Here is a solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isMultiplyPrime(int a) {
        if (a < 2) {
            return false;
        }
        int count = 0;
        for (int i = 2; i <= a / i; i++) {
            while (a % i == 0) {
                a /= i;
                count++;
                if (count > 3) {
                    return false;
                }
            }
        }
        if (a > 1) {
            count++;
            if (count > 3) {
                return false;
            }
        }
        return count == 3;
    }
}
```

This function first checks if the given number is less than 2, in which case it returns false as there are no prime numbers less than 2.

Then it uses a loop to check if the given number is divisible by any number from 2 to `a / i`. If it is, it divides `a` by `i` and increments the count of prime numbers. If the count of prime numbers is greater than 3, it returns false.

After the loop, if `a` is greater than 1, it means that `a` is a prime number and it increments the count of prime numbers. If the count of prime numbers is greater than 3, it returns false.

Finally, if the count of prime numbers is equal to 3, it returns true as the given number is the multiplication of 3 prime numbers.