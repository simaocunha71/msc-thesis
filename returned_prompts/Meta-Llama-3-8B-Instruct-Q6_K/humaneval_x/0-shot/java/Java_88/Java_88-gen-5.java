Here is a Java solution:

```java
import java.util.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        int sum = array.get(0) + array.get(array.size() - 1);
        List<Integer> copy = new ArrayList<>(array);

        if (sum % 2 == 0) {
            Collections.sort(copy, Collections.reverseOrder());
        } else {
            Collections.sort(copy);
        }

        return copy;
    }
}
```

In this solution, we first calculate the sum of the first and last elements of the array. If the sum is even, we sort the array in descending order; otherwise, we sort it in ascending order. We use the `Collections.sort` method to sort the array and the `Collections.reverseOrder` method to sort it in descending order. We then return the sorted array. We don't change the original array, so we create a copy of it before sorting.

Note that this solution assumes that the input array is not empty. If the input array is empty, the solution will throw a `NoSuchElementException` when trying to get the first or last element. If you want to handle the case where the input array is empty, you can add a check at the beginning of the method to return an empty list. For example:

```java
if (array.isEmpty()) {
    return new ArrayList<>();
}
```

This way, the method will return an empty list if the input array is empty, instead of throwing an exception.