```java
import java.util.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        List<Integer> copy = new ArrayList<>(array);
        int sum = copy.get(0) + copy.get(copy.size() - 1);
        if (sum % 2 == 0) {
            Collections.sort(copy, Collections.reverseOrder());
        } else {
            Collections.sort(copy);
        }
        return copy;
    }
}
```

Explanation:
The problem asks to create a copy of the given array and sort it in ascending order if the sum of the first and last elements of the array is odd, or sort it in descending order if the sum is even. We use the `Collections.sort()` method to sort the array. If the sum is even, we use the `reverseOrder()` method to sort the array in descending order.

We create a copy of the given array using `new ArrayList<>(array)` to avoid modifying the original array. We calculate the sum of the first and last elements of the array using `copy.get(0) + copy.get(copy.size() - 1)`. Then, we check if the sum is even or odd using the modulo operator `%`. If the sum is even, we sort the array in descending order using `Collections.sort(copy, Collections.reverseOrder())`. If the sum is odd, we sort the array in ascending order using `Collections.sort(copy)`.

Finally, we return the sorted copy of the array.