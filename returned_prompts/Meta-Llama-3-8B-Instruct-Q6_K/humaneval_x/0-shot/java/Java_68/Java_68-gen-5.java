Here is a Java solution using a simple loop to iterate over the array and find the smallest even value.

```java
import java.util.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        List<Integer> result = new ArrayList<>();
        int smallestValue = Integer.MAX_VALUE;
        int smallestIndex = -1;
        
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) % 2 == 0 && arr.get(i) < smallestValue) {
                smallestValue = arr.get(i);
                smallestIndex = i;
            }
        }
        
        if (smallestValue != Integer.MAX_VALUE) {
            result.add(smallestValue);
            result.add(smallestIndex);
        } else {
            result.add([]);
        }
        
        return result;
    }
}
```

This solution works by initializing `smallestValue` to `Integer.MAX_VALUE` and `smallestIndex` to `-1`. Then it iterates over the array, checking if each value is even and smaller than `smallestValue`. If it is, it updates `smallestValue` and `smallestIndex`. Finally, if `smallestValue` is not `Integer.MAX_VALUE`, it adds `smallestValue` and `smallestIndex` to the result list. If `smallestValue` is still `Integer.MAX_VALUE`, it adds an empty list to the result. The result is then returned.

The time complexity of this solution is O(n), where n is the size of the input array, because it iterates over the array once. The space complexity is O(1), because it uses a constant amount of space to store the result and the indices.