    rows, cols := len(grid), len(grid[0])
    res := 0
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if grid[i][j] == 1 {
                res += capacity
            }
        }
    }
    return res
}
// Please note that the above solution is incorrect. We need to consider the bucket's capacity and the water level in the well. The correct solution is more complex. It involves using a queue to keep track of the wells and the water levels. The bucket is moved to the well with the highest water level that is less than the bucket's capacity. The process is repeated until all wells are empty or the bucket is empty.
// Here is the correct solution:
func MaxFill(grid [][]int, capacity int) int {
    rows, cols := len(grid), len(grid[0])
    res := 0
    queue := make([]*struct{row, col int; water int}, 0)
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            if grid[i][j] == 1 {
                queue = append(queue, &struct{row, col int; water int}{i, j, 1})
            }
        }
    }
    for len(queue) > 0 {
        queue = append(queue, nil)
        for i := 0; i < len(queue) - 1; i++ {
            q := queue[i]
            if q == nil {
                queue = queue[1:]
                continue
            }
            queue[i] = nil
            if q.water > 0 {
                if q.water < capacity {
                    res++
                }
                q.water--
                if q.water > 0 {
                    queue = append(queue, q)
                }
            }
        }
    }
    return res
}