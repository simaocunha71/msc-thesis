Here is a solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int solution(List<Integer> lst) {
        int sum = 0;
        for (int i = 0; i < lst.size(); i += 2) {
            if (lst.get(i) % 2 != 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}
```

This solution iterates over the list by skipping every other element (i.e., elements at even indices) and checks if the current element is odd. If it is, the element is added to the sum. Finally, the sum is returned.

In the examples you provided, the function would return:

```java
solution(Arrays.asList(5, 8, 7, 1)) ==> 12 (5 + 7)
solution(Arrays.asList(3, 3, 3, 3, 3)) ==> 9 (3 + 3 + 3)
solution(Arrays.asList(30, 13, 24, 321)) ==> 0 (no odd elements at even positions)
```