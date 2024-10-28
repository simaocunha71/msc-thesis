The problem is asking to add the even elements that are at odd indices from the given list of integers.

Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public int add(List<Integer> lst) {
        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (i % 2 != 0 && lst.get(i) % 2 == 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}
```

In this solution, we are iterating over the list using a for loop. For each element, we are checking if the index is odd (i.e., `i % 2 != 0`) and if the element is even (i.e., `lst.get(i) % 2 == 0`). If both conditions are true, we add the element to the sum. Finally, we return the sum. 

The time complexity of this solution is O(n), where n is the size of the list, as we are iterating over the list once. The space complexity is O(1), as we are using a constant amount of space to store the sum. 

The example you provided, `add(Arrays.asList(4, 2, 6, 7))`, would return `2` because the even elements at odd indices are `2` and `6`, and `2 + 6 = 8`. However, the problem statement asks to add only the even elements that are at odd indices, so the correct answer is `2`. 