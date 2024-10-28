Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public boolean monotonic(List<Integer> l) {
        boolean increasing = true;
        boolean decreasing = true;

        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) > l.get(i - 1)) {
                decreasing = false;
            }
            if (l.get(i) < l.get(i - 1)) {
                increasing = false;
            }
        }

        return increasing || decreasing;
    }
}
```

In this solution, we iterate through the list and check if each element is greater or lesser than the previous one. If we find any pair of adjacent elements where one is greater and the other is lesser, we set the corresponding boolean variable to `false`. At the end, we return `true` if either `increasing` or `decreasing` is `true`, meaning that the list is either increasing or decreasing monotonically. If both are `false`, the list is neither increasing nor decreasing, so we return `false`.