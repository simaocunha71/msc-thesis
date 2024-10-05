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
1. We iterate over each number in the list.
2. For each number, we use the `Math.ceil()` function to round it up to the nearest integer.
3. We then square the rounded number by multiplying it by itself.
4. We add the squared number to our running total `sum`.
5. Finally, we return the total sum of squares.

This solution has a time complexity of O(n), where n is the number of elements in the list, as we iterate over each element once. The space complexity is O(1), as we only use a constant amount of space to store the sum.