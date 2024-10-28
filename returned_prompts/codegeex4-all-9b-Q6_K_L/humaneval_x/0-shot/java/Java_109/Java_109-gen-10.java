```java
import java.util.*;

class Solution {
    public boolean moveOneBall(List<Integer> arr) {
        if (arr.size() == 0) return true;
        int minIndex = 0;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) < arr.get(minIndex)) {
                minIndex = i;
            }
        }
        for (int i = minIndex + 1; i < arr.size(); i++) {
            if (arr.get(i) < arr.get(i - 1)) {
                return false;
            }
        }
        for (int i = 0; i < minIndex; i++) {
            if (arr.get(i) > arr.get(i + 1)) {
                return false;
            }
        }
        return true;
    }
}
```

I have added a solution for the problem. 

The approach is to find the index of the minimum element in the array. Then, check if the elements to the right of the minimum element are sorted in non-decreasing order. Also, check if the elements to the left of the minimum element are sorted in non-decreasing order. If both conditions are satisfied, then the array can be sorted by performing right shift operations.