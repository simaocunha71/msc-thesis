```java
import java.util.*;

class Solution {
    public int sumSquares(List<Double> lst) {
        int sum = 0;
        for (Double num : lst) {
            int ceil = (int) Math.ceil(num);
            sum += Math.pow(ceil, 2);
        }
        return sum;
    }
}
```

Explanation:
The problem is asking to find the sum of squared numbers in a given list, but before squaring, each number needs to be rounded up to the nearest integer. This can be achieved using the Math.ceil function.

In the given code, a for-each loop is used to iterate over the list of Double numbers. For each number, Math.ceil is used to round it up to the nearest integer, and then the squared value of the integer is added to the sum.

Finally, the sum is returned as an integer. This solution works for both positive and negative numbers, as well as decimal numbers. The Math.pow function is used to calculate the square of the rounded integer. The result is an integer, which is the sum of the squared numbers.