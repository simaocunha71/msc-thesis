Here is a Java solution using a greedy approach:

```java
public int maxFill(List<List<Integer>> grid, int capacity) {
    int result = 0;
    for (List<Integer> row : grid) {
        int sum = 0;
        for (int water : row) {
            sum += water;
        }
        result += (sum + capacity - 1) / capacity; // round up to the nearest integer
    }
    return result;
}
```

This function iterates over each row in the grid and calculates the total amount of water in the row. It then adds the number of times you need to lower the bucket (calculated as `(sum + capacity - 1) / capacity`) to the result. The reason for `(sum + capacity - 1)` is to ensure that we round up the division, as we need to lower the bucket even if there is only a tiny bit of water left in the well.

The time complexity of this solution is O(n*m), where n is the number of rows and m is the number of columns in the grid. The space complexity is O(1), as we are only using a constant amount of extra space.