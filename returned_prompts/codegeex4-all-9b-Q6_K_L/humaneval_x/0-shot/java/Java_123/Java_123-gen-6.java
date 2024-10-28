```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> getOddCollatz(int n) {
        Set<Integer> collatz = new HashSet<>();
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
            if (n % 2 != 0) {
                collatz.add(n);
            }
        }
        collatz.add(1);
        List<Integer> result = new ArrayList<>(collatz);
        Collections.sort(result);
        return result;
    }
}
```
This solution works by first initializing a set to store the odd numbers in the Collatz sequence. Then, it enters a loop that continues until `n` reaches 1. If `n` is even, it divides `n` by 2; if `n` is odd, it multiplies `n` by 3 and adds 1. If `n` is odd, it adds `n` to the set. After the loop, it adds 1 to the set and converts the set to a list, which is then sorted in ascending order and returned.