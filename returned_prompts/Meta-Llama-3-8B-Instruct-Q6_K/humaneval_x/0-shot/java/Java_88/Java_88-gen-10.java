Here is a Java solution using the `Collections.sort()` method:

```java
import java.util.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        if (array.isEmpty()) {
            return array;
        }
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

In this solution, we first check if the array is empty. If it is, we simply return the array as it is. Then we calculate the sum of the first and last elements of the array. If the sum is even, we sort the array in descending order using `Collections.sort()` with `Collections.reverseOrder()` as the comparator. If the sum is odd, we sort the array in ascending order using `Collections.sort()` with no comparator. Finally, we create a new `ArrayList` from the sorted array and return it. This approach ensures that the original array is not modified.