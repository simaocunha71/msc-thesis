```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        if (arr.isEmpty()) {
            return new ArrayList<>();
        }
        
        int smallestEvenValue = Integer.MAX_VALUE;
        int smallestEvenIndex = -1;
        
        for (int i = 0; i < arr.size(); i++) {
            int value = arr.get(i);
            if (value % 2 == 0) {
                if (value < smallestEvenValue) {
                    smallestEvenValue = value;
                    smallestEvenIndex = i;
                }
            }
        }
        
        if (smallestEvenIndex == -1) {
            return new ArrayList<>();
        } else {
            return Arrays.asList(smallestEvenValue, smallestEvenIndex);
        }
    }
}
```