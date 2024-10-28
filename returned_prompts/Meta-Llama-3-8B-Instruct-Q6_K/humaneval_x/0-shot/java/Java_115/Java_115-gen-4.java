Here is a possible solution in Java:

```java
public int maxFill(List<List<Integer>> grid, int capacity) {
    int rows = grid.size();
    int cols = grid.get(0).size();
    int count = 0;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid.get(i).get(j) == 1) {
                count += capacity;
            }
        }
    }

    return count;
}
```

The solution iterates over each well in the grid and adds the capacity of each well to the total count if the well is filled (i.e., the value at the well's position is 1). The total count is then returned as the result.

For example, given the grid `[[0,0,1,0], [0,1,0,0], [1,1,1,1]]` and a bucket capacity of 1, the function would return 6, because the filled wells are:

* The third well in the first row (value 1)
* The second well in the second row (value 1)
* The first, second, and third wells in the third row (values 1, 1, and 1)

Each of these wells would require the bucket to be lowered once to empty it, so the total count is 6.