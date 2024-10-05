Here is a Java solution for the problem:

```java
import java.util.*;

public class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        Set<Integer> set1 = new HashSet<Integer>(l1);
        Set<Integer> set2 = new HashSet<Integer>(l2);
        set1.retainAll(set2);
        List<Integer> result = new ArrayList<Integer>(set1);
        Collections.sort(result);
        return result;
    }
}
```

This solution first converts the input lists to sets for efficient lookup and intersection. It then retains the elements of the first set that are also in the second set, and converts the resulting set back to a list. Finally, it sorts the list and returns it. The time complexity of this solution is O(n log n), where n is the total number of elements in the input lists. This is because the retainAll operation takes O(n) time, and the sort operation takes O(n log n) time. The space complexity is O(n), where n is the number of unique elements in the input lists. This is because the solution needs to store the unique elements in the result list. 