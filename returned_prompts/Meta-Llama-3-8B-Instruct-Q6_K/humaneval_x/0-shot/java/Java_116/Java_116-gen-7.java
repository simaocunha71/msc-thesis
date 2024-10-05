Here is the solution to the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        Collections.sort(arr, (a, b) -> {
            int onesA = Integer.bitCount(a);
            int onesB = Integer.bitCount(b);

            if (onesA == onesB) {
                return Integer.compare(a, b);
            } else {
                return Integer.compare(onesA, onesB);
            }
        });
        return arr;
    }
}
```

This solution uses the `Collections.sort()` method to sort the array. The sorting is done based on the number of ones in the binary representation of each number. If the number of ones is the same for two numbers, they are sorted based on their decimal value. The `Integer.bitCount()` method is used to count the number of ones in the binary representation of a number. The `Integer.compare()` method is used to compare the decimal values of two numbers. The lambda expression `(a, b) -> { ... }` is used to specify the comparator for the sorting. The comparator first compares the number of ones, and if they are the same, it compares the decimal values. The sorted array is then returned.