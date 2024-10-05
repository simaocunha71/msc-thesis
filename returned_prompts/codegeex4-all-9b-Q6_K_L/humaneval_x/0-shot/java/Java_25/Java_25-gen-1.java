Here is the solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> factorize(int n) {
        List<Integer> factors = new ArrayList<>();
        for (int i = 2; i <= n / i; i++) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }
        if (n > 1) {
            factors.add(n);
        }
        return factors;
    }
}
```

This solution works by iterating through all numbers from 2 to the square root of the given number. For each number, it checks if it is a factor of the given number. If it is, it adds it to the list of factors and divides the given number by it. This process is repeated until the given number is no longer divisible by the current number. If the given number is still greater than 1 after this process, it means that the given number is a prime number and is added to the list of factors. The list of factors is then returned.

Note: This solution assumes that the input number is greater than 1. If the input number can be less than or equal to 1, additional checks should be added to handle this case.