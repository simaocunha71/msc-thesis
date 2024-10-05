```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> factorize(int n) {
        List<Integer> result = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                result.add(i);
                n /= i;
            }
        }
        return result;
    }
}
```

Explanation:
1. We initialize an empty list `result` to store the prime factors.
2. We iterate from 2 to `n` (inclusive) using a for loop.
3. For each number `i`, we check if `n` is divisible by `i` using the modulus operator `%`.
4. If `n` is divisible by `i`, we add `i` to the `result` list and update `n` to `n / i`.
5. We repeat steps 3 and 4 until `n` is no longer divisible by `i`.
6. Finally, we return the `result` list which contains the prime factors of `n`.