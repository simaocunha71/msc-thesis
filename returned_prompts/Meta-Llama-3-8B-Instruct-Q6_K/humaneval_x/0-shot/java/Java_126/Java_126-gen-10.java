Here is a Java solution using a single loop:

```java
import java.util.*;

class Solution {
    public boolean isSorted(List<Integer> lst) {
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i - 1) >= lst.get(i)) {
                return false;
            }
        }
        return true;
    }
}
```

This solution iterates through the list, comparing each element with the previous one. If it finds an element that is less than or equal to the previous one, it returns false, indicating that the list is not sorted. If it doesn't find any such element after iterating through the entire list, it returns true, indicating that the list is sorted.

Note that this solution assumes that the list contains only positive integers, as per the problem statement. If the list can contain negative numbers or non-integer values, additional checks would be needed.

Also, this solution has a time complexity of O(n), where n is the size of the list, because it only needs to iterate through the list once to check if it's sorted. The space complexity is O(1), because it only uses a constant amount of space to store the loop variable and the list reference.