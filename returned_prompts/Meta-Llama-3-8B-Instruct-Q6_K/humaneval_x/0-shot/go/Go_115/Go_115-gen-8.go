Here is a simple solution in Go:

```go
func MaxFill(grid [][]int, capacity int) int {
    totalWater := 0
    for _, row := range grid {
        totalWater += sum(row)
    }
    return totalWater / capacity
}

func sum(row []int) int {
    total := 0
    for _, v := range row {
        total += v
    }
    return total
}
```

This solution first calculates the total amount of water in all wells by summing up the 1's in each row. Then it divides this total by the capacity of the buckets to get the number of times the buckets need to be lowered.

The time complexity is O(m*n), where m is the number of rows and n is the number of columns in the grid, because we are summing up all the elements in the grid. The space complexity is O(1), because we are using a constant amount of space to store the total amount of water and the sum of each row.