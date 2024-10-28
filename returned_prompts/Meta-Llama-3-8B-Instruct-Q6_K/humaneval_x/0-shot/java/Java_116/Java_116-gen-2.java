Here is the solution:
```java
import java.util.*;

class Solution {
    public List<Integer> sortArray(List<Integer> arr) {
        Collections.sort(arr, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                int onesA = Integer.toBinaryString(a).replace("0", "").length();
                int onesB = Integer.toBinaryString(b).replace("0", "").length();
                if (onesA == onesB) {
                    return a - b;
                } else {
                    return onesA - onesB;
                }
            }
        });
        return arr;
    }
}
```
Explanation:
This solution uses the `Collections.sort()` method to sort the list of integers. The `Comparator` interface is used to define the sorting criteria. In this case, the criteria is based on the number of ones in the binary representation of each integer.

The `compare()` method is implemented to compare two integers `a` and `b`. It first calculates the number of ones in the binary representation of each integer using the `Integer.toBinaryString()` method and the `replace()` method. If the number of ones is the same for both integers, the method returns the result of `a - b`, which sorts the integers based on their decimal value. If the number of ones is different, the method returns the result of `onesA - onesB`, which sorts the integers based on the number of ones in their binary representation.

Finally, the sorted list is returned. This solution has a time complexity of O(n log n), where n is the size of the input list. This is because the `Collections.sort()` method uses a sorting algorithm (such as Timsort) that has a time complexity of O(n log n) in the worst case. The space complexity is O(1), as the solution only uses a constant amount of space to store the sorting criteria.