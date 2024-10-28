The problem can be solved by using a greedy approach. We can iterate over the grid and fill the bucket with water as much as possible. Then we can lower the bucket to empty it. We can repeat this process until the grid is empty.

Here is the implementation in Java:

```java
import java.util.*;

class Solution {
    public int maxFill(List<List<Integer>> grid, int capacity) {
        int count = 0;
        for (List<Integer> row : grid) {
            int sum = 0;
            for (int cell : row) {
                sum += cell;
            }
            while (sum > 0) {
                int min = Math.min(sum, capacity);
                sum -= min;
                count++;
            }
        }
        return count;
    }
}
```

This solution works by iterating over each row in the grid, calculating the total amount of water in the row, and then filling the bucket with as much water as possible. The bucket is then lowered by the amount of water it contains, and the process is repeated until the row is empty. The number of times the bucket is lowered is the number of times the bucket needs to be lowered to empty the row. The total number of times the bucket is lowered is the result.

The time complexity of this solution is O(m * n), where m is the number of rows in the grid and n is the number of columns. This is because we need to iterate over each cell in the grid once. The space complexity is O(1), as we only use a constant amount of space to store the sum of the row and the count of the number of times the bucket is lowered. 