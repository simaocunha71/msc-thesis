Here is the Java code to solve the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int solution(List<Integer> lst) {
        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (i % 2 == 0 && lst.get(i) % 2 != 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}
```

In this code, we iterate over the list. If the index `i` is even and the element at index `i` is odd, we add it to the sum. Finally, we return the sum.

Here is how the code works:

- We initialize the sum to 0.
- We iterate over the list using a for loop.
- For each element, we check if the index is even and the element is odd.
- If the element is odd and the index is even, we add the element to the sum.
- Finally, we return the sum.