Here is a Java solution to the problem:

```java
public int maxFill(List<List<Integer>> grid, int capacity) {
    int max = 0;
    for (List<Integer> list : grid) {
        int sum = 0;
        for (int i : list) {
            sum += i;
        }
        if (sum > max) {
            max = sum;
        }
    }
    return (max + capacity - 1) / capacity;
}
```

This solution works by calculating the total amount of water in each well (row) and then finding the maximum amount of water. The number of times the buckets need to be lowered is then calculated by dividing the maximum amount of water by the bucket's capacity and rounding up. This is done by adding capacity - 1 to the maximum amount of water before dividing by the capacity.

Note: This solution assumes that the grid is a rectangular grid of wells. If the grid is not rectangular, the solution will not work correctly.