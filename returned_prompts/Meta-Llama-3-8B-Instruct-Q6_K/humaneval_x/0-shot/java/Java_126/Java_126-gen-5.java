Here is a Java solution:

```java
import java.util.*;

class Solution {
    public boolean isSorted(List<Integer> lst) {
        if (lst.size() <= 1) {
            return true;
        }
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i - 1) > lst.get(i)) {
                return false;
            }
            if (Collections.frequency(lst, lst.get(i)) > 1) {
                return false;
            }
        }
        return true;
    }
}
```

This solution checks if the list is sorted in ascending order and if there are no more than one duplicate of the same number. If the list has less than or equal to one element, it is considered sorted. The solution then iterates over the list, checking if each element is less than or equal to the previous one, and if there are more than one duplicate of the same number. If it finds an element that is not less than or equal to the previous one, or if it finds a duplicate of the same number, it returns false. If it iterates over the entire list without finding any issues, it returns true. 