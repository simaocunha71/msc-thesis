```java
import java.util.*;
import java.lang.*;

class Solution {
    public int smallestChange(List<Integer> arr) {
        int left = 0;
        int right = arr.size() - 1;
        int changes = 0;

        while (left < right) {
            if (arr.get(left) != arr.get(right)) {
                changes++;
            }
            left++;
            right--;
        }

        return changes;
    }
}
```