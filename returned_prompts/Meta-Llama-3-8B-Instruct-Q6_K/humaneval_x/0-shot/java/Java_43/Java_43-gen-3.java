Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public boolean pairsSumToZero(List<Integer> l) {
        Set<Integer> set = new HashSet<>();
        for (int num : l) {
            if (set.contains(-num)) {
                return true;
            }
            set.add(num);
        }
        return false;
    }
}
```

Explanation:
The problem is asking to find if there are two distinct elements in the list that sum to zero. 

We can use a HashSet to keep track of the elements we have seen so far. For each element in the list, we check if -num is in the set. If it is, that means we have found two elements that sum to zero, and we return true. If we finish iterating through the list and haven't found any such pair, we return false.

The time complexity is O(n) where n is the size of the list, because we are doing a constant amount of work for each element in the list. The space complexity is also O(n) because in the worst case, we might have to store all elements in the set. 