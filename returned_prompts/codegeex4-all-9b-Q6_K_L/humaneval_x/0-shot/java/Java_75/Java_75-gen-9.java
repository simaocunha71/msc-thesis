```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isMultiplyPrime(int a) {
        int count = 0;
        for (int i = 2; i <= Math.sqrt(a); i++) {
            if (a % i == 0) {
                count++;
                a /= i;
                i--;
            }
        }
        return count == 3;
    }
}
```
The above code checks if the given number is the multiplication of 3 prime numbers. It first divides the given number by all the numbers less than its square root. If the number is divisible by any of these numbers, it increments a counter and divides the number by that number. It repeats this process until the number becomes 1 or less than 2. If the counter is equal to 3, it means that the given number is the multiplication of 3 prime numbers and it returns true. Otherwise, it returns false.