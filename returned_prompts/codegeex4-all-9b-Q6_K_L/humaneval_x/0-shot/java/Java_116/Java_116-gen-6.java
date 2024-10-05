Here's one possible implementation of the sortArray method:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        // Sort the array based on the number of ones in the binary representation
        Collections.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                // Count the number of ones in the binary representation of a and b
                int countA = Integer.bitCount(a);
                int countB = Integer.bitCount(b);

                // If the number of ones is the same, compare the decimal values
                if (countA == countB) {
                    return a.compareTo(b);
                }

                // Otherwise, compare based on the number of ones
                return Integer.compare(countA, countB);
            }
        });

        return arr;
    }
}
```

This implementation uses the `Collections.sort` method to sort the array. The `Comparator` is implemented as an anonymous inner class that compares two integers based on the number of ones in their binary representation. If the number of ones is the same, the integers are compared based on their decimal values.