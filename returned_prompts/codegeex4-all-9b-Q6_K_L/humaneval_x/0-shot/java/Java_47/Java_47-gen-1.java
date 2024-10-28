Here is a Java solution using the Collections.sort() method to sort the list in ascending order and then checking the size of the list to determine the median.

```java
import java.util.*;

public class Solution {
    public double median(List<Integer> l) {
        // Sort the list in ascending order
        Collections.sort(l);

        // Find the size of the list
        int size = l.size();

        // Check if the size is even or odd
        if (size % 2 == 0) {
            // If the size is even, return the average of the two middle numbers
            return (l.get(size / 2 - 1) + l.get(size / 2)) / 2.0;
        } else {
            // If the size is odd, return the middle number
            return l.get(size / 2);
        }
    }
}
```
This solution has a time complexity of O(n log n) due to the sorting operation.