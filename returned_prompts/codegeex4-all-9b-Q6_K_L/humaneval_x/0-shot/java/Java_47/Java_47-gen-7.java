```java
import java.util.*;
import java.lang.*;

class Solution {
    public double median(List<Integer> l) {
        // Sort the list
        Collections.sort(l);
        int n = l.size();
        // Check if the number of elements is odd or even
        if (n % 2 == 0) {
            // If even, return the average of the two middle elements
            return (l.get(n / 2 - 1) + l.get(n / 2)) / 2.0;
        } else {
            // If odd, return the middle element
            return l.get(n / 2);
        }
    }
}
```