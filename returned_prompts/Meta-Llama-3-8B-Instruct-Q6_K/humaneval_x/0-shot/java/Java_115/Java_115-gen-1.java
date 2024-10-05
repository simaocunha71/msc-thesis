```java
import java.util.*;

class Solution {
    public int maxFill(List<List<Integer>> grid, int capacity) {
        int count = 0;
        for (List<Integer> row : grid) {
            int water = 0;
            for (int cell : row) {
                water += cell;
            }
            count += (water / capacity) + (water % capacity > 0 ? 1 : 0);
        }
        return count;
    }
}
```
Explanation:
1. Initialize a variable `count` to keep track of the total number of times the buckets need to be lowered.
2. Iterate through each row in the grid.
3. Calculate the total amount of water in the current row by summing up all the cells.
4. Calculate the number of times the bucket needs to be lowered for the current row by dividing the total water by the bucket capacity and rounding up to the nearest integer using the formula `(water / capacity) + (water % capacity > 0 ? 1 : 0)`.
5. Add the result to the `count` variable.
6. Return the final `count` value.

This solution works by iterating through each row in the grid, calculating the total amount of water in each row, and then calculating the number of times the bucket needs to be lowered for each row. The bucket capacity is used to determine how many times the bucket needs to be lowered for each row, and the formula `(water / capacity) + (water % capacity > 0 ? 1 : 0)` is used to round up to the nearest integer. The final result is the total number of times the bucket needs to be lowered across all rows.