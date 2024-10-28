Here is the Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        // If list is empty, return empty list
        if (lst.isEmpty()) {
            return lst;
        }

        // Sort the list
        Collections.sort(lst);

        // Initialize result list
        List<Integer> res = new ArrayList<>();

        // Initialize two pointers
        int i = 0, j = lst.size() - 1;

        // Alternate between adding from start and end of list
        while (i <= j) {
            res.add(lst.get(i));
            if (i != j) {
                res.add(lst.get(j));
            }
            i++;
            j--;
        }

        // If list has odd number of elements, add middle element
        if (i == j + 1) {
            res.add(lst.get(i));
        }

        return res;
    }
}
```

This solution first sorts the list in ascending order. Then, it initializes two pointers at the start and end of the list. It alternates between adding elements from the start and end of the list to the result list. If the list has an odd number of elements, it adds the middle element to the result list.

For example, if the input list is [1, 2, 3, 4], the sorted list is [1, 2, 3, 4]. The result list is [1, 4, 2, 3].