Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public boolean triplesSumToZero(List<Integer> l) {
        Set<Integer> set = new HashSet<>(l);
        for (int num : set) {
            if (set.contains(-num) && set.contains(num * 2)) {
                return true;
            }
        }
        return false;
    }
}
```

Explanation:
The solution iterates over the set of distinct elements in the list. For each element, it checks if the set contains both the negative of the element and the element multiplied by 2. If it does, it returns true, because this means there are three distinct elements in the list that sum to zero. If it doesn't find such a combination, it returns false. This solution has a time complexity of O(n), where n is the number of distinct elements in the list. The space complexity is also O(n), because it uses a set to store the distinct elements.