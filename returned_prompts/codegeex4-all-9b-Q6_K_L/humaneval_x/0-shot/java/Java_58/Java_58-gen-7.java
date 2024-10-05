```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        // Convert both lists to sets to remove duplicates and allow for efficient lookup
        Set<Integer> set1 = new HashSet<>(l1);
        Set<Integer> set2 = new HashSet<>(l2);

        // Find the intersection of the two sets
        set1.retainAll(set2);

        // Convert the set back to a list and sort it
        List<Integer> result = new ArrayList<>(set1);
        Collections.sort(result);

        return result;
    }
}
```
