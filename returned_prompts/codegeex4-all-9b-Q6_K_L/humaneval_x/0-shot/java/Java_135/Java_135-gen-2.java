Here is a Java solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int canArrange(List<Integer> arr) {
        int maxIndex = -1;
        for(int i = 0; i < arr.size() - 1; i++) {
            if(arr.get(i) > arr.get(i+1)) {
                maxIndex = i;
            }
        }
        return maxIndex;
    }
}
```

This function iterates over the list, comparing each element with the next one. If it finds an element that is greater than the next one, it sets the maxIndex to the current index. At the end, it returns the maxIndex. If no such element is found, the maxIndex remains -1.