Here is the solution for the problem:

```java
import java.util.*;

class Solution {
    public boolean triplesSumToZero(List<Integer> l) {
        Set<Integer> set = new HashSet<>(l);
        for (Integer i : set) {
            Set<Integer> set2 = new HashSet<>(set);
            set2.remove(i);
            for (Integer j : set2) {
                Set<Integer> set3 = new HashSet<>(set2);
                set3.remove(j);
                if (set3.contains(-i - j)) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

This solution uses a set to store the elements in the list to avoid duplicates and to make the lookup operation more efficient. Then it iterates over the set and for each element, it removes it from the set and then iterates over the remaining elements to find a pair that sums up to the negation of the current element. If such a pair is found, the function returns true. If no such triple is found after checking all possible combinations, the function returns false.

The time complexity of this solution is O(n^2) where n is the number of elements in the list, and the space complexity is O(n) for storing the set. The space complexity can be improved to O(1) by removing the set and using a boolean array to keep track of the elements that have been seen so far. However, this would make the solution more complex and harder to understand. The current solution is simpler and more efficient in terms of space complexity.