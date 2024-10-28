    n, m := len(grid), len(grid[0]);
    queue := [][]int{{0, 0, 0, 0, 0}};
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] == 1 {
                queue = append(queue, []int{i, j, grid[i][j], 0, 0})
            }
        }
    }
    cnt := 0;
    for len(queue) > 0 {
        cnt++
        qlen := len(queue)
        for i := 0; i < qlen; i++ {
            x, y, water, step, prevX := queue[i][0], queue[i][1], queue[i][2], queue[i][3], queue[i][4];
            if step == capacity {
                queue = append(queue, []int{x, y, 0, 0, prevX})
                grid[prevX][y] += water
                grid[x][y] -= water
            } else {
                if grid[x][y + 1] == 1 {
                    queue = append(queue, []int{x, y + 1, grid[x][y + 1], step + 1, x})
                }
                if grid[x+1][y] == 1 {
                    queue = append(queue, []int{x + 1, y, grid[x+1][y], step + 1, x})
                }
            }
        }
    }
    return cnt - 1
}

/*
Test
Next:
1. Test edge cases
2. Test corner cases
3. Test with many wells
4. Test with different capacity
5. Test with different grid size
6. Test with different grid values
*/

func ExampleMaxFill() {
    grid := [][]int{{0, 0, 1, 0}, {0, 1, 0, 0}, {1, 1, 1, 1}}
    fmt.Println(MaxFill(grid,