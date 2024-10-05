Here is a Java solution that uses a helper function to check if a number is prime. It iterates from 2 to n-1 and checks if each number is prime. If it is, it adds it to the result list.

```java
import java.util.*;

class Solution {
    public List<Integer> countUpTo(int n) {
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
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

In the above code, we first initialize an empty list `result` to store the prime numbers. Then we iterate from 2 to `n-1`. For each number `i` in this range, we check if it is prime using the `isPrime` function. If it is, we add it to the `result` list. Finally, we return the `result` list.

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, it is not a prime number. If it is not divisible by any of these values, it is a prime number. This function returns `true` if the number is prime and `false` otherwise.