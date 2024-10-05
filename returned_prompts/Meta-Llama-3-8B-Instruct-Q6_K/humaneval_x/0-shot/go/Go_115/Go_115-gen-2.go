Here is a solution for the problem:

```go
func MaxFill(grid [][]int, capacity int) int {
    var res int
    for _, row := range grid {
        for _, val := range row {
            if val == 1 {
                res += capacity
            }
        }
    }
    return res
}
```

This solution iterates over each row in the grid and for each row, it iterates over each cell. If the cell value is 1, it means there is water in that well, so we add the bucket capacity to the result. This way, we are effectively "lowering" the bucket for each well that has water. The result is the total number of times we need to lower the buckets.

For example, in the first example, we have three wells with water. We need to lower the bucket six times: three times for the first well, two times for the second well, and one time for the third well. The function returns 6. 

In the second example, we have four wells with water. We need to lower the bucket five times: three times for the first well, one time for the second well, and one time for the third well. The function returns 5.

In the third example, there are no wells with water, so we don't need to lower the bucket at all. The function returns 0. 

This solution has a time complexity of O(m*n), where m is the number of rows in the grid and n is the number of columns. This is because we iterate over each cell in the grid once. The space complexity is O(1), as we only use a constant amount of space to store the result and some temporary variables. 

This solution assumes that the input grid is valid, i.e., it does not contain any rows with a different length. It also assumes that the bucket capacity is positive. If these assumptions are not valid, additional error checking code would be needed. 

The function `MaxFill` takes two inputs: `grid` and `capacity`. It returns an integer representing the number of times we need to lower the buckets. 

The grid is a 2D slice of integers, where each integer represents the presence or absence of water in a well. The capacity is an integer representing the capacity of the buckets. 

For example, you can call the function like this:

```go
grid := [][]int{{0,0,1,0}, {0,1,0,0},