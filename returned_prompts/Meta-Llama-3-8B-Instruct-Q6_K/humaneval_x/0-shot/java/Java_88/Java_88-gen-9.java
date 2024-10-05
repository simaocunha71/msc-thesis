Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        int sum = array.get(0) + array.get(array.size() - 1);
        if (sum % 2 == 0) {
            Collections.sort(array, Collections.reverseOrder());
        } else {
            Collections.sort(array);
        }
        return new ArrayList<>(array);
    }
}
```
Here's an explanation of the solution:

1. Calculate the sum of the first and last elements of the array.
2. If the sum is even, sort the array in descending order using `Collections.sort(array, Collections.reverseOrder())`.
3. If the sum is odd, sort the array in ascending order using `Collections.sort(array)`.
4. Create a new `ArrayList` from the original array and return it.

This solution is O(n log n) due to the sorting operation, where n is the size of the array. The space complexity is O(n) because we create a new `ArrayList` to return the sorted result.