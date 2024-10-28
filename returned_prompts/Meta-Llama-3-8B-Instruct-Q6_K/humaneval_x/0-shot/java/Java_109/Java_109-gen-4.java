Here is the Java code for the problem:

```java
import java.util.*;

class Solution {
    public boolean moveOneBall(List<Integer> arr) {
        if (arr.isEmpty()) {
            return true;
        }

        int min = Collections.min(arr);
        int max = Collections.max(arr);

        if (min == max) {
            return true;
        }

        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) != min + i) {
                return false;
            }
        }

        return true;
    }
}
```

This solution works by first checking if the array is empty. If it is, the function returns true because an empty array is considered to be sorted.

Then, it finds the minimum and maximum values in the array. If the minimum and maximum values are the same, the array is already sorted, so the function returns true.

Finally, it checks if the array is sorted by comparing each element to the minimum value plus the current index. If any element is not equal to this value, the function returns false. If the function finishes checking all elements without returning false, it returns true, indicating that the array can be sorted by performing right shift operations.