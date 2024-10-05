Here is a Java solution for the problem:

```java
public int maxFill(List<List<Integer>> grid, int capacity) {
    int sum = 0;
    for (List<Integer> row : grid) {
        sum += Math.ceil((double) row.stream().reduce(0, Integer::sum) / capacity);
    }
    return sum;
}
```

In this solution, we iterate over each row of the grid. For each row, we calculate the sum of all the ones in the row, which represents the total amount of water in that row. We then divide this sum by the bucket's capacity, which gives us the number of times we need to lower the bucket to empty the row. We use Math.ceil to round up to the nearest whole number, as we cannot have a fraction of a bucket fill.

Finally, we sum up all the bucket fills required for each row and return this sum as the result.