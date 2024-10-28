This problem can be solved by iterating through the array and checking if the current element is greater than the previous one. If it's not, then we can't get a non-decreasing order by performing right shift operations. Here's the solution in Java:

```java
import java.util.*;

class Solution {
    public boolean moveOneBall(List<Integer> arr) {
        if (arr.isEmpty()) {
            return true;
        }
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) < arr.get(i - 1)) {
                return false;
            }
        }
        return true;
    }
}
```

This solution works by iterating through the array and checking if the current element is less than the previous one. If it is, then the array is not sorted in non-decreasing order, so the function returns false. If the loop completes without finding any such pair, then the array is sorted in non-decreasing order, so the function returns true. If the array is empty, the function returns true as per the problem statement.

The time complexity of this solution is O(n), where n is the size of the input array, as we are iterating through the array once. The space complexity is O(1), as we are not using any extra space that scales with the input size.