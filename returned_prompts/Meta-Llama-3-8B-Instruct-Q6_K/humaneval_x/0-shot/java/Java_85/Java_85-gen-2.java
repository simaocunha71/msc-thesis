The problem is asking to add the even numbers that are at odd indices in the given list of integers.

Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public int add(List<Integer> lst) {
        int sum = 0;
        for (int i = 1; i < lst.size(); i += 2) {
            if (lst.get(i) % 2 == 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}
```

In this solution, we iterate over the list with a step of 2, starting from the second element (index 1). For each element at an odd index, we check if it's even by using the modulus operator (%). If the element is even, we add it to the sum. Finally, we return the sum. 

For example, if the input list is `[4, 2, 6, 7]`, the output will be `2` because `2` is the only even number at an odd index in the list. 