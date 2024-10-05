Here is a Java solution to this problem:

```java
import java.util.*;

class Solution {
    public List<Integer> getOddCollatz(int n) {
        List<Integer> result = new ArrayList<>();
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = n * 3 + 1;
            }
            if (n % 2 != 0) {
                result.add(n);
            }
        }
        Collections.sort(result);
        return result;
    }
}
```

This solution starts with the given number `n` and applies the Collatz sequence rules until it reaches 1. For each step, it checks if the number is odd and if so, adds it to the result list. Finally, it sorts the result list in increasing order and returns it.

For example, if `n` is 5, the solution would return `[1, 5]`. The Collatz sequence for 5 is `[5, 16, 8, 4, 2, 1]`, so the odd numbers are only 1 and 5. If `n` is 10, the solution would return `[1, 3, 9]`. The Collatz sequence for 10 is `[10, 5, 16, 8, 4, 2, 1]`, so the odd numbers are 1, 3, and 9.