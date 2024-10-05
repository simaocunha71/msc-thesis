Here is the solution in Java using Java 8 Stream API:

```java
import java.util.*;

class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        // Convert lists to sets for efficient intersection operation
        Set<Integer> set1 = new HashSet<>(l1);
        Set<Integer> set2 = new HashSet<>(l2);

        // Find common elements
        Set<Integer> commonElements = new HashSet<>(set1);
        commonElements.retainAll(set2);

        // Convert set back to list and sort it
        List<Integer> result = new ArrayList<>(commonElements);
        Collections.sort(result);

        return result;
    }
}
```

The time complexity is O(n) where n is the sum of the sizes of the two lists, as we are converting the lists to sets in linear time. The space complexity is also O(n), as we are storing the common elements in a set and then converting it back to a list. The `retainAll` operation takes O(m) time where m is the size of the smaller set, which is the dominant operation in the time complexity. The `sort` operation takes O(m log m) time, but it is not the dominant operation in the time complexity. 