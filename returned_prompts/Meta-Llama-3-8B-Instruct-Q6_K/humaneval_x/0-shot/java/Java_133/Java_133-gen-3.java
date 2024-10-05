```java
import java.util.*;

class Solution {
    public int sumSquares(List<Double> lst) {
        int sum = 0;
        for (Double num : lst) {
            int ceilNum = (int) Math.ceil(num);
            sum += Math.pow(ceilNum, 2);
        }
        return sum;
    }
}
```
Explanation:
The problem requires you to calculate the sum of the squares of the elements in the given list. However, the problem statement also mentions that you need to round each element in the list to the upper integer (ceiling) first. 

We can achieve this by using the Math.ceil() function in Java, which returns the smallest integer greater than or equal to the given number. We then square the ceiling of each number and add it to the sum.

In the solution, we initialize a variable sum to 0. Then, we iterate over each element in the list using a for-each loop. For each element, we calculate its ceiling using Math.ceil() and cast it to an integer. We then square this integer and add it to the sum. Finally, we return the sum.

For example, if the input list is [1.4, 4.2, 0], the output will be 29. Here's the calculation:
- For 1.4, the ceiling is 2, so we add 2^2 = 4 to the sum.
- For 4.2, the ceiling is 5, so we add 5^2 = 25 to the sum.
- For 0, the ceiling is still 0, so we add 0^2 = 0 to the sum.
- The total sum is 4 + 25 + 0 = 29.