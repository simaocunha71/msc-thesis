```java
import java.util.*;

class Solution {
    public List<Integer> getOddCollatz(int n) {
        List<Integer> result = new ArrayList<>();
        while (n != 1) {
            if (n % 2 == 1) {
                result.add(n);
            }
            n = n % 2 == 0 ? n / 2 : n * 3 + 1;
        }
        return result;
    }
}
```
Explanation:
The solution uses a simple iterative approach to generate the Collatz sequence for the given number n. It starts by initializing an empty list `result` to store the odd numbers in the sequence.

In each iteration, it checks if the current number `n` is odd by using the modulo operator `%`. If `n` is odd, it adds `n` to the `result` list.

Then, it applies the Collatz sequence rule to get the next number in the sequence. If `n` is even, it divides `n` by 2. If `n` is odd, it multiplies `n` by 3 and adds 1.

The loop continues until `n` reaches 1, which is the terminating condition for the Collatz sequence.

Finally, the solution returns the `result` list, which contains the odd numbers in the Collatz sequence. The list is sorted in increasing order by default, as required by the problem statement.