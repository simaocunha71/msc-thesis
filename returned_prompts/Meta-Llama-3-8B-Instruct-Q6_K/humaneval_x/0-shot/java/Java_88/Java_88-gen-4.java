Here is the Java code for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        int sum = array.get(0) + array.get(array.size() - 1);
        List<Integer> sortedArray = new ArrayList<>(array);
        if (sum % 2 == 0) {
            Collections.sort(sortedArray, Collections.reverseOrder());
        } else {
            Collections.sort(sortedArray);
        }
        return sortedArray;
    }
}
```

The solution works as follows:

1. First, it calculates the sum of the first and last elements of the array.
2. Then, it creates a copy of the original array.
3. If the sum is even, it sorts the copied array in descending order.
4. If the sum is odd, it sorts the copied array in ascending order.
5. Finally, it returns the sorted array. The original array remains unchanged.