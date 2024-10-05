Here is a Java solution for the problem:

```java
import java.util.*;

class Solution {
    public int sumSquares(List<Double> lst) {
        int sum = 0;
        for (double num : lst) {
            sum += (int) Math.ceil(num) * (int) Math.ceil(num);
        }
        return sum;
    }
}
```

This solution iterates over each element in the list, rounds it to the upper integer using `Math.ceil`, squares the rounded number, and adds it to the sum. The result is the sum of squared numbers in the list, rounded to the upper integer first. 

For example, if the input list is `[1.4, 4.2, 0]`, the function will round each element to the upper integer: `[2, 5, 1]`, then square each element: `[4, 25, 1]`, and finally add them up: `4 + 25 + 1 = 30`. The function returns `30`. 

The function uses the `Math.ceil` method to round each element to the upper integer, and the `int` cast to convert the result to an integer. The function returns the sum as an integer. 

The time complexity of this solution is O(n), where n is the number of elements in the list, because it iterates over each element once. The space complexity is O(1), because it uses a constant amount of space to store the sum. 