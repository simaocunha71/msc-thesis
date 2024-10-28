Here is the solution:
```java
import java.util.*;

class Solution {
    public int maxFill(List<List<Integer>> grid, int capacity) {
        int rows = grid.size();
        int cols = grid.get(0).size();
        int count = 0;
        for (int i = 0; i < rows; i++) {
            int water = 0;
            for (int j = 0; j < cols; j++) {
                water += grid.get(i).get(j);
            }
            count += water / capacity;
            if (water % capacity > 0) {
                count++;
            }
        }
        return count;
    }
}
```
Explanation:

1. First, we calculate the total number of rows and columns in the grid.
2. Then, we iterate over each row in the grid.
3. For each row, we calculate the total amount of water in that row by summing up all the 1's in the row.
4. We then divide the total amount of water by the bucket capacity to get the number of times we can fill the buckets.
5. If there is any remaining water after filling the buckets, we increment the count by 1.
6. Finally, we return the total count of times we need to lower the buckets.

Time complexity: O(rows \* cols)

Space complexity: O(1) (since we are not using any extra space that scales with the input size) 