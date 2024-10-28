```java
import java.util.*;
import java.util.stream.*;

public class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst.size() < 2) {
            return Optional.empty();
        }
        lst.sort(Integer::compareTo);
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) != lst.get(i - 1)) {
                return Optional.of(lst.get(i));
            }
        }
        return Optional.empty();
    }
}
```
Explanation:

*   We first check if the list has less than 2 elements. If it does, we return an empty optional as there's no 2nd smallest element.
*   We sort the list in ascending order.
*   We then iterate over the sorted list, starting from the 2nd element (index 1). We check if the current element is different from the previous one. If it is, we return the current element as the 2nd smallest.
*   If we reach the end of the list without finding a unique element (i.e., all elements are the same), we return an empty optional.

This solution has a time complexity of O(n log n) due to the sorting, where n is the size of the input list. The space complexity is O(1) as we only use a constant amount of space.