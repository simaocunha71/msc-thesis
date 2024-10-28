```java
import java.util.*;
import java.lang.*;

class Solution {
    public int smallestChange(List<Integer> arr) {
        if (arr == null || arr.size() == 0) {
            return 0;
        }
        
        int count = 0;
        int left = 0;
        int right = arr.size() - 1;
        
        while (left < right) {
            if (arr.get(left) != arr.get(right)) {
                count++;
            }
            left++;
            right--;
        }
        
        return count;
    }
}
```