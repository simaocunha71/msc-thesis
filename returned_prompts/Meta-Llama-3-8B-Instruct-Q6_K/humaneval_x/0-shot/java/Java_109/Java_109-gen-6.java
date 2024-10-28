```java
import java.util.*;

public class Solution {
    public boolean moveOneBall(List<Integer> arr) {
        int i = 0, j = arr.size() - 1;
        while (i < j) {
            if (arr.get(i) > arr.get(i + 1)) {
                return false;
            }
            if (arr.get(j) < arr.get(j - 1)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
```

Explanation:
This solution uses two pointers, one at the start of the array (i) and one at the end (j). It checks if the elements at these positions are in the correct order (i.e., the element at the start is less than or equal to the element at the next position, and the element at the end is greater than or equal to the element at the previous position). If it finds an inversion, it returns false. If it goes through the entire array without finding an inversion, it returns true.

The reason why this solution works is because a right shift operation can only move elements that are greater than the one it is shifting. Therefore, if the array is not sorted, there must be at least one element that is greater than the one next to it, which means that right shift operations cannot produce a sorted array. On the other hand, if the array can be sorted by right shift operations, then it must be possible to move all elements to their correct positions, which means that the array is sorted. Therefore, if the array is not sorted, the function returns false, and if the array is sorted, it returns true.

Time complexity: O(n), where n is the size of the array.
Space complexity: O(1), as we only use a constant amount of space to store the two pointers. 