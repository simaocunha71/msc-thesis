```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> getOddCollatz(int n) {
        Set<Integer> oddNumbers = new HashSet<>();
        while (n != 1) {
            if (n % 2 == 1) {
                oddNumbers.add(n);
            }
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
        }
        oddNumbers.add(1);
        List<Integer> result = new ArrayList<>(oddNumbers);
        Collections.sort(result);
        return result;
    }
}
```
The given code is a Java solution for the problem. It defines a class `Solution` with a method `getOddCollatz(int n)`. 

The method first initializes a `HashSet` called `oddNumbers` to store the odd numbers in the Collatz sequence. Then, it enters a while loop that continues until `n` becomes 1. 

In each iteration of the loop, it checks if `n` is odd or even. If `n` is odd, it adds `n` to the `oddNumbers` set. If `n` is even, it divides `n` by 2. If `n` is odd, it multiplies `n` by 3 and adds 1. 

After the loop ends, it adds 1 to the `oddNumbers` set and converts it to an `ArrayList` called `result`. It then sorts `result` in increasing order and returns it. 

The time complexity of this solution is O(n), where n is the input number.