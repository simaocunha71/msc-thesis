The problem is asking you to find the minimum number of times you need to lower the buckets to empty the wells. You can solve this problem by iterating over each well and calculating the total amount of water in that well. Then, you can divide the total amount of water by the bucket capacity and round up to the nearest integer to find the number of times you need to lower the buckets for that well. Finally, you can sum up the results for all wells to get the total number of times you need to lower the buckets.

Here is the Java solution for the problem:
```
public int maxFill(List<List<Integer>> grid, int capacity) {
    int maxFill = 0;
    for (List<Integer> well : grid) {
        int totalWater = 0;
        for (int water : well) {
            totalWater += water;
        }
        maxFill += (totalWater + capacity - 1) / capacity;
    }
    return maxFill;
}
```
This solution works by iterating over each well in the grid and calculating the total amount of water in that well. Then, it divides the total amount of water by the bucket capacity and rounds up to the nearest integer using the `(totalWater + capacity - 1) / capacity` formula. Finally, it sums up the results for all wells to get the total number of times you need to lower the buckets.

For example, if the input grid is `[[0,0,1,0], [0,1,0,0], [1,1,1,1]]` and the bucket capacity is 1, the output will be 6, which is the minimum number of times you need to lower the buckets to empty the wells.

Note that this solution assumes that the bucket capacity is a positive integer and that the grid is not empty. You may want to add error checking code to handle these cases if necessary.