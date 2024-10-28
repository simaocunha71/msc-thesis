Here is a Java solution for the problem:

```java
import java.util.*;

class Solution {
    public int maxFill(List<List<Integer>> grid, int capacity) {
        int rows = grid.size();
        int cols = grid.get(0).size();
        int rowsFilled = 0;
        int colsFilled = 0;
        int maxFill = 0;

        // Count the number of rows and columns filled
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid.get(i).get(j) == 1) {
                    rowsFilled++;
                    colsFilled++;
                }
            }
        }

        // Calculate the maximum fill
        maxFill = (rowsFilled + colsFilled) / capacity;

        return maxFill;
    }
}
```

This solution works by first counting the number of rows and columns filled in the grid. It then calculates the maximum fill by dividing the sum of the rows and columns filled by the bucket capacity. The result is the minimum number of times the buckets need to be lowered to empty the wells. The time complexity of this solution is O(m*n), where m is the number of rows and n is the number of columns in the grid. The space complexity is O(1), as it only uses a constant amount of space.