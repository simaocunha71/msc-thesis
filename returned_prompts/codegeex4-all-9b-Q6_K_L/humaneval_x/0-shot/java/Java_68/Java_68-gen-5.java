```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        // Check if the array is empty
        if (arr.size() == 0) {
            return new ArrayList<Integer>();
        }
        
        // Initialize variables to store the smallest even value and its index
        int smallestEven = Integer.MAX_VALUE;
        int smallestEvenIndex = -1;
        
        // Iterate through the array
        for (int i = 0; i < arr.size(); i++) {
            // Check if the current value is even and smaller than the current smallest even value
            if (arr.get(i) % 2 == 0 && arr.get(i) < smallestEven) {
                smallestEven = arr.get(i);
                smallestEvenIndex = i;
            }
        }
        
        // Check if a smallest even value was found
        if (smallestEvenIndex == -1) {
            return new ArrayList<Integer>();
        }
        
        // Return the smallest even value and its index
        return Arrays.asList(smallestEven, smallestEvenIndex);
    }
}
```