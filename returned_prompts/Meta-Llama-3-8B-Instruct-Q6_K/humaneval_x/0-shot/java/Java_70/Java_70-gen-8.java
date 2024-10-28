```java
import java.util.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        if (lst.isEmpty()) {
            return lst;
        }
        Collections.sort(lst);
        List<Integer> result = new ArrayList<>();
        while (!lst.isEmpty()) {
            result.add(lst.get(0));
            lst.remove(0);
            if (!lst.isEmpty()) {
                lst.sort((a, b) -> b - a);
                result.add(lst.get(0));
                lst.remove(0);
            }
        }
        return result;
    }
}
```

Explanation:
The problem is asking to implement a strange sorting algorithm that starts with the minimum value, then the maximum of the remaining integers, then the minimum again, and so on.

Here is a simple Java solution for this problem:

First, we sort the input list in ascending order. Then, we create a new list to store the result. We iterate over the input list, and for each iteration, we add the smallest element to the result list, then remove it from the input list. If the input list is not empty after removing the smallest element, we sort the remaining elements in descending order, add the largest element to the result list, and remove it from the input list. This process continues until the input list is empty.

The time complexity of this solution is O(n log n) due to the sorting operations, where n is the size of the input list. The space complexity is O(n) for storing the result list.