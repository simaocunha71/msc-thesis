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
Explanation:
The solution first calculates the sum of the first and last elements of the given array. If the sum is even, it sorts the array in descending order; otherwise, it sorts the array in ascending order. Finally, it returns a copy of the sorted array.

The `Collections.sort()` method is used to sort the array. If the second argument is `null`, it sorts the array in ascending order. If the second argument is `Collections.reverseOrder()`, it sorts the array in descending order.

The `new ArrayList<>(array)` expression is used to create a copy of the array. This is necessary because the `Collections.sort()` method sorts the array in place, meaning that it modifies the original array. By creating a copy of the array, we ensure that the original array remains unchanged.