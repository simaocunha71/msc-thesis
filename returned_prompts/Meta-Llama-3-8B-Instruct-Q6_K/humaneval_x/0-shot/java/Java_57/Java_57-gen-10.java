Here is a simple solution in Java that checks if a list of integers is monotonically increasing or decreasing:

```java
import java.util.*;

class Solution {
    public boolean monotonic(List<Integer> l) {
        boolean increasing = true;
        boolean decreasing = true;
        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) > l.get(i - 1)) {
                decreasing = false;
            } else if (l.get(i) < l.get(i - 1)) {
                increasing = false;
            }
        }
        return increasing || decreasing;
    }
}
```

This solution iterates through the list and checks if the current element is greater or less than the previous element. If it is greater, it means the list is not decreasing. If it is less, it means the list is not increasing. If the list is neither increasing nor decreasing, it will return false. Otherwise, it will return true.

This solution has a time complexity of O(n), where n is the size of the list, because it iterates through the list once. It has a space complexity of O(1), because it uses a constant amount of space to store the two boolean variables.