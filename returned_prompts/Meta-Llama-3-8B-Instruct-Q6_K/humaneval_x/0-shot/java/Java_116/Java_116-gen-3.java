Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        Collections.sort(arr, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                int countA = Integer.toBinaryString(a).replace("0", "").length();
                int countB = Integer.toBinaryString(b).replace("0", "").length();
                if (countA == countB) {
                    return a - b;
                } else {
                    return countA - countB;
                }
            }
        });
        return arr;
    }
}
```

Explanation:
This solution uses the `Collections.sort` method with a custom `Comparator` to sort the array. The `Comparator` is implemented as an anonymous inner class that compares two integers `a` and `b`. It calculates the number of ones in the binary representation of each integer using `Integer.toBinaryString(a).replace("0", "").length()`. If the number of ones is the same for both integers, it compares them based on their decimal value. If the number of ones is different, it compares them based on the number of ones. The `Collections.sort` method uses this `Comparator` to sort the array. The sorted array is then returned. 