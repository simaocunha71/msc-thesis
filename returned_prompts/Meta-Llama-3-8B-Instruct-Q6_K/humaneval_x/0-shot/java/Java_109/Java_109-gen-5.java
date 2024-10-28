Here is a Java solution to the problem:

```java
import java.util.*;

class Solution {
    public boolean moveOneBall(List<Integer> arr) {
        if (arr.isEmpty()) {
            return true;
        }
        int min = Collections.min(arr);
        int max = Collections.max(arr);
        int moves = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) != min + i) {
                return false;
            }
        }
        return true;
    }
}
```

Explanation:

The problem is asking if it is possible to sort the given array in non-decreasing order by performing right shift operations. The right shift operation moves the last element of the array to the starting position.

We can solve this problem by iterating through the array and checking if each element is at its correct position. If an element is not at its correct position, it means that it is not possible to sort the array by performing right shift operations.

In the given solution, we first find the minimum and maximum values in the array. Then, we iterate through the array and check if each element is at its correct position. If an element is not at its correct position, we return false. If we successfully iterate through the array without returning false, we return true, indicating that it is possible to sort the array by performing right shift operations.

The time complexity of this solution is O(n), where n is the size of the array, because we are iterating through the array once. The space complexity is O(1), because we are using a constant amount of space to store the minimum and maximum values. 