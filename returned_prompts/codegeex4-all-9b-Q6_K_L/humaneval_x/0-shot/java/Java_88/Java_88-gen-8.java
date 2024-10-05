```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        if (array.size() <= 1) return array;

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

Explanation:
1. First, we check if the given array has only one or no element. If it does, we return the array as it is since there's nothing to sort.
2. We calculate the sum of the first and last elements of the array.
3. We create a copy of the given array and store it in a new list called `sortedArray`.
4. If the sum is even, we sort the `sortedArray` in descending order using `Collections.sort()` with `Collections.reverseOrder()`.
5. If the sum is odd, we sort the `sortedArray` in ascending order using `Collections.sort()`.
6. Finally, we return the sorted `sortedArray`.