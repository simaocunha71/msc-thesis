Here is the solution:

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
The problem is asking to check if there are three distinct elements in the list that sum to zero. To solve this, we can use a set to remove duplicates and then iterate over the set.

We check if the set contains the negative of the current number and the double of the current number. If both conditions are met, it means we have found three numbers that sum to zero, so we return true.

If we iterate over the entire set and don't find such numbers, we return false.

The time complexity of this solution is O(n), where n is the size of the input list. This is because we are iterating over the set once. The space complexity is also O(n), as we are storing the input list in a set.