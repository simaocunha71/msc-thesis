Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        Collections.sort(arr, (a, b) -> {
            int countA = Integer.toBinaryString(a).replace("0", "").length();
            int countB = Integer.toBinaryString(b).replace("0", "").length();
            if (countA == countB) {
                return Integer.compare(a, b);
            } else {
                return Integer.compare(countA, countB);
            }
        });
        return arr;
    }
}
```

This solution uses the `Collections.sort()` method, which sorts the list based on the comparator provided. In this case, the comparator compares two integers `a` and `b` as follows:

* First, it calculates the number of ones in the binary representation of `a` and `b` using the `Integer.toBinaryString()` method and the `replace()` method.
* If the number of ones is the same for both `a` and `b`, it compares the decimal values of `a` and `b` using the `Integer.compare()` method.
* If the number of ones is different, it compares the number of ones.

The `Collections.sort()` method then sorts the list based on this comparator. The sorted list is returned as the result.