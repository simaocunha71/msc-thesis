```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> countUpTo(int n) {
        if (n <= 1) {
            return new ArrayList<>();
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                result.add(i);
            }
        }
        return result;
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
The function `countUpTo` takes an integer `n` as input and returns a list of prime numbers less than `n`. It checks each number from 2 to `n-1` to see if it is prime using the `isPrime` helper function. The `isPrime` function checks if a number is divisible by any number from 2 to its square root. If it is divisible by any number, it returns false, otherwise it returns true.