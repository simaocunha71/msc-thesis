```java
import java.util.*;

class Solution {
    public int sumSquares(List<Double> lst) {
        int sum = 0;
        for (double num : lst) {
            sum += Math.ceil(num) * Math.ceil(num);
        }
        return sum;
    }
}
```

Explanation:
This Java program takes a list of double numbers as input and returns the sum of the squares of the upper integer of each number.

The `Math.ceil(num)` function is used to round each element in the list to the upper int(Ceiling). Then, it squares each number and adds it to the sum.

The time complexity of this solution is O(n), where n is the number of elements in the input list, as it needs to iterate over each element in the list once. The space complexity is O(1), as it only uses a constant amount of space to store the sum.