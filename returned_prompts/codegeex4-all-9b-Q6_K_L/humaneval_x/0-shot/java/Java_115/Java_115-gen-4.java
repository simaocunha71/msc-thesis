```java
import java.util.*;

class Solution {
    public int maxFill(List<List<Integer>> grid, int capacity) {
        int sum = 0;
        for (List<Integer> row : grid) {
            int rowSum = 0;
            for (int i : row) {
                rowSum += i;
            }
            sum += rowSum / capacity;
        }
        return sum;
    }
}
```