Here is a solution that uses a two-pointer approach to find the maximum number of times the buckets need to be lowered:
```go
func MaxFill(grid [][]int, capacity int) int {
    m, n := len(grid), len(grid[0])
    var res int
    for i := 0; i < m; i++ {
        left, right := 0, 0
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                right++
            } else {
                left++
            }
        }
        res += int(math.Min(float64(left), float64(right)) / float64(capacity))
    }
    return res
}
```
Here's an explanation of the solution:

* We iterate over each row of the grid.
* For each row, we maintain two pointers: `left` and `right`. `left` points to the first 0 in the row, and `right` points to the first 1 in the row.
* We move `left` and `right` until they meet, which means we've filled the bucket with water.
* We add the number of times we need to lower the bucket to the result.
* We repeat this process for each row.

The time complexity of this solution is O(m \* n), where m is the number of rows and n is the number of columns in the grid. The space complexity is O(1), as we only use a constant amount of space to store the result and the two pointers.