```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isSorted(List<Integer> lst) {
        // Check if list is empty or has only one element
        if (lst.size() <= 1) {
            return true;
        }

        // Check if list has duplicates
        Set<Integer> set = new HashSet<>();
        for (int num : lst) {
            if (set.contains(num)) {
                return false;
            }
            set.add(num);
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