The task is to sort an array of non-negative integers according to the number of ones in their binary representation in ascending order. If there are similar numbers of ones, then sort based on decimal value.

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

In this solution, we use the `Collections.sort()` method with a custom `Comparator` to sort the array. The `compare()` method of the `Comparator` is used to compare two elements. It first calculates the number of ones in the binary representation of each element using the `Integer.toBinaryString()` method. If the number of ones is the same for both elements, then it compares the decimal values of the elements. If the number of ones is different, then it compares the number of ones. The `Collections.sort()` method uses the `compare()` method to sort the array. The sorted array is then returned.