Here is a Java solution that checks if the list is sorted in ascending order and if it has more than one duplicate of the same number:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isSorted(List<Integer> lst) {
        // Check if list is empty
        if (lst.isEmpty()) {
            return true;
        }

        // Check if list has more than one duplicate of the same number
        Set<Integer> set = new HashSet<>(lst);
        if (lst.size() != set.size()) {
            return false;
        }

        // Check if list is sorted in ascending order
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < lst.get(i - 1)) {
                return false;
            }
        }

        return true;
    }
}
```

In this solution, we first check if the list is empty. If it is, we return `true` since an empty list is considered to be sorted.

Next, we create a `HashSet` from the list. A `HashSet` is a collection that contains no duplicate elements. If the size of the `HashSet` is not equal to the size of the list, it means that the list has more than one duplicate of the same number, so we return `false`.

Finally, we iterate through the list and check if each element is greater than or equal to the previous element. If we find an element that is less than the previous element, we return `false`.

If we make it through all the elements without returning `false`, it means that the list is sorted in ascending order, so we return `true`.