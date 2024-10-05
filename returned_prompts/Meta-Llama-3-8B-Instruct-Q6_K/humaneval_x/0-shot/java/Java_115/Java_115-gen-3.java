The problem is asking to find the minimum number of times you need to lower the buckets to empty the wells. 

Here is the solution:

```java
public int maxFill(List<List<Integer>> grid, int capacity) {
    int count = 0;
    for (List<Integer> row : grid) {
        int totalWater = 0;
        for (int water : row) {
            totalWater += water;
        }
        count += totalWater / capacity + (totalWater % capacity > 0 ? 1 : 0);
    }
    return count;
}
```

Explanation:

*   We iterate over each row of the grid.
*   For each row, we calculate the total water in the row by summing up all the values.
*   We then calculate how many times the bucket needs to be lowered to empty the well by doing integer division of the total water by the bucket capacity.
*   If there is any remaining water (i.e., `totalWater % capacity > 0`), we add 1 to the count because we need to lower the bucket one more time to empty the remaining water.
*   We add the count of the current row to the total count.
*   Finally, we return the total count.

This solution has a time complexity of O(m*n), where m is the number of rows in the grid and n is the number of columns in the grid, because we iterate over each element in the grid once. The space complexity is O(1), because we only use a constant amount of space to store the count and the total water. 