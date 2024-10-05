Here is a Java solution to the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        List<Integer> result = new ArrayList<>();
        if (lst.isEmpty()) return result;
        Collections.sort(lst);
        int i = 0, j = lst.size() - 1;
        boolean minFirst = true;
        while (i <= j) {
            if (minFirst) result.add(lst.get(i++));
            else result.add(lst.get(j--));
            minFirst = !minFirst;
        }
        return result;
    }
}
```

This solution first sorts the input list `lst`. Then it starts from both ends of the list and alternately adds the minimum and maximum remaining elements to the result list. This continues until all elements from the input list are added to the result list.

The time complexity of this solution is O(n log n) due to the sorting operation, where n is the length of the input list. The space complexity is O(n) for storing the result list.