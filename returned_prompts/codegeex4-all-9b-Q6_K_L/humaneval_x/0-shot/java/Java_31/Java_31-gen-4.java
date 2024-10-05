```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```
The code checks if a given number `n` is prime by iterating from 2 to the square root of `n` and checking if `n` is divisible by any of these numbers. If `n` is divisible by any number in this range, it is not prime and the function returns false. If `n` is not divisible by any number in this range, it is prime and the function returns true.