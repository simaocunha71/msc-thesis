Here's a Java implementation for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        // Convert lists to sets to remove duplicates and allow for fast lookup
        Set<Integer> set1 = new HashSet<>(l1);
        Set<Integer> set2 = new HashSet<>(l2);

        // Find intersection of the two sets
        Set<Integer> commonElements = new HashSet<>(set1);
        commonElements.retainAll(set2);

        // Convert the set back to a list and sort it
        List<Integer> result = new ArrayList<>(commonElements);
        Collections.sort(result);

        return result;
    }
}
```

This implementation first converts the input lists to sets to remove duplicate values and allow for fast lookup. It then finds the intersection of the two sets, which gives us the common elements. Finally, it converts the set back to a list and sorts it before returning the result.