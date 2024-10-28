Here is a Java function that solves the problem:

```java
import java.util.*;

class Solution {
    public int canArrange(List<Integer> arr) {
        int n = arr.size();
        int max = 0;
        for (int i = 0; i < n; i++) {
            if (arr.get(i) > max) {
                max = arr.get(i);
            }
        }
        for (int i = 1; i < n; i++) {
            if (arr.get(i) >= arr.get(i - 1)) {
                return i - 1;
            }
        }
        return -1;
    }
}
```

This function iterates over the array to find the maximum value. Then it iterates over the array again to find the largest index of an element which is not greater than or equal to the element immediately preceding it. If no such element exists, it returns -1. The given array will not contain duplicate values.

The time complexity of this function is O(n), where n is the size of the array. The space complexity is O(1), as it only uses a constant amount of space.