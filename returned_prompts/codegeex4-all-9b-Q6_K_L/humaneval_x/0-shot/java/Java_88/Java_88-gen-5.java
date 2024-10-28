```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        // if the array is empty, return an empty array
        if (array.isEmpty()) {
            return Collections.emptyList();
        }
        // calculate the sum of the first and last elements
        int sum = array.get(0) + array.get(array.size() - 1);
        // create a copy of the given array
        List<Integer> copy = new ArrayList<>(array);
        // if the sum is even, sort the copy in descending order
        if (sum % 2 == 0) {
            Collections.sort(copy, Collections.reverseOrder());
        } else {
            // if the sum is odd, sort the copy in ascending order
            Collections.sort(copy);
        }
        // return the sorted copy
        return copy;
    }
}
```