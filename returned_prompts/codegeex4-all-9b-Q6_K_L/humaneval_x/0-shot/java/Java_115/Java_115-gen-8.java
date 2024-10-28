Here is a possible solution in Java:

```java
public int maxFill(List<List<Integer>> grid, int capacity) {
    int total = 0;
    for (List<Integer> row : grid) {
        for (int i = 0; i < row.size(); i++) {
            if (row.get(i) == 1) {
                int count = 1;
                while (count <= capacity && i + count < row.size() && row.get(i + count) == 1) {
                    count++;
                }
                total += (count + (count - 1)) / 2; // add the number of buckets needed to fill the well
                i += count - 1; // skip the wells that have been filled
            }
        }
    }
    return total;
}
```

The solution works as follows:

- It iterates over each row in the grid.
- For each row, it iterates over each well in the row.
- If the well has water (i.e., the value is 1), it counts the number of consecutive wells that have water.
- It then calculates the number of buckets needed to fill the well, which is the sum of the first (count + 1) / 2 integers, where count is the number of consecutive wells that have water.
- It adds the number of buckets needed to fill the well to the total.
- It then skips the wells that have been filled by adding count - 1 to the current well index.
- Finally, it returns the total number of buckets needed to fill all the wells.