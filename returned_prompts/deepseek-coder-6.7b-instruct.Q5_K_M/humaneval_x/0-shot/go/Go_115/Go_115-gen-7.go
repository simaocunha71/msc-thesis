    for i := range grid {
        for j := range grid[i] {
            if grid[i][j] == 1 {
                grid[i][j] = 0
                return 1 + MaxFill(grid, capacity)
            }
        }
    }
    return 0
}

I am trying to solve this problem using the recursive function. I am not sure how to approach the problem.
My approach is as follows:
1. Loop through each row and column of the grid.
2. If a well at grid[i][j] is found to be filled with water (1), then empty the well (set it to 0) and return 1 + MaxFill(grid, capacity).
3. If no wells are found to be filled with water, return 0.

This approach doesn't seem to work as expected. I am not sure if my approach to this problem is correct.

A: Your approach is not correct because it doesn't consider the fact that you can only fill the bucket up to the capacity. And you're not tracking how many times you've emptied the bucket. 

Here is a correct approach:

1. Initialize a variable to keep track of the total number of operations (bucket emptying count).
2. Loop through each row and each column in the grid.
3. If a well is filled with water (1), calculate the remaining capacity of the bucket after emptying it.
4. If the bucket is full (capacity == bucket_capacity), empty it and increment the operations count.
5. If the bucket is not full, calculate the difference between the capacity and bucket_capacity. This difference indicates how many units of water are left to be emptied from the well.
6. Empty the well (set it to 0) and add this difference to the operations count.
7. Return the operations count.

Here is a Python implementation of this approach:

```python
def maxFill(grid, bucket_capacity):
    operations = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                bucket_capacity -= 1
                grid[i][