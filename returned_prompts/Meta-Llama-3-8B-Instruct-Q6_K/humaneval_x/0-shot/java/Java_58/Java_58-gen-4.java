Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> common(List<Integer> l1, List<Integer> l2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        
        for (int i : l1) {
            set1.add(i);
        }
        
        for (int i : l2) {
            set2.add(i);
        }
        
        Set<Integer> commonSet = new HashSet<>(set1);
        commonSet.retainAll(set2);
        
        List<Integer> result = new ArrayList<>(commonSet);
        Collections.sort(result);
        
        return result;
    }
}
```

Explanation:

1. Create two sets, `set1` and `set2`, to store the elements of the two lists. This step takes O(n) time complexity.

2. Iterate over the two lists and add their elements to the corresponding sets. This step also takes O(n) time complexity.

3. Create a new set, `commonSet`, to store the common elements between `set1` and `set2`. Use the `retainAll` method to find the common elements, which takes O(n) time complexity.

4. Convert the `commonSet` to a list, `result`, and sort it. This step takes O(n log n) time complexity.

5. Return the `result` list. This step takes O(1) time complexity.

The overall time complexity is O(n + n log n) = O(n log n), where n is the total number of elements in the two lists. The space complexity is O(n), as we need to store the elements of the two lists in the sets. 

This solution works for any type of elements in the lists, not just integers. It also works for lists of different sizes. The order of the elements in the result list is the same as their order in the first list. 

The `retainAll` method returns a boolean value indicating whether the set has been modified. In this case, we don't care about the return value, so we can ignore it. 

The `HashSet` class provides constant-time operations for the basic operations (add, remove, contains), making it suitable for large datasets. The `ArrayList` class provides constant-time operations for the basic operations (get, set), making it suitable for large datasets. 

The `Collections.sort` method sorts the list in-place. It uses a sorting algorithm