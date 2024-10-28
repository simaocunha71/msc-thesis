Here is a Java solution to the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int canArrange(List<Integer> arr) {
        // Sort the array in ascending order
        Collections.sort(arr);
        
        // Iterate through the array
        for (int i = 1; i < arr.size(); i++) {
            // If the current element is not greater than the previous element, return the current index
            if (arr.get(i) < arr.get(i - 1)) {
                return i - 1;
            }
        }
        
        // If no such element exists, return -1
        return -1;
    }
}
```

The function first sorts the array in ascending order. Then it iterates through the array and checks if the current element is not greater than the previous element. If it finds such an element, it returns the index of the previous element. If it doesn't find such an element, it returns -1.