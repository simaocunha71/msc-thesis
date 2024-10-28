To solve this problem, we can iterate through each row of the grid and calculate the number of buckets needed for each row. We can then sum up the number of buckets needed for all the rows to get the total number of buckets needed.

Here is the Java code to solve this problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int maxFill(List<List<Integer>> grid, int capacity) {
        int numBuckets = 0;
        for (List<Integer> row : grid) {
            int numUnits = 0;
            for (int unit : row) {
                numUnits += unit;
            }
            numBuckets += (numUnits + capacity - 1) / capacity; // round up to nearest multiple of capacity
        }
        return numBuckets;
    }
}
```

In this code, we first initialize the number of buckets to 0. Then, we iterate through each row of the grid. For each row, we calculate the total number of units of water in the row by summing up all the units. We then divide the total number of units by the bucket capacity and round up to the nearest multiple of the bucket capacity to get the number of buckets needed for that row. We add the number of buckets needed for each row to the total number of buckets. Finally, we return the total number of buckets needed.