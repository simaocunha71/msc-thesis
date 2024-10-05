    m := len(grid)
    n := len(grid[0])

    // bfs
    q := [][]int{}
    cnt := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                q = append(q, []int{i, j})
                cnt++
            }
        }
    }
    if cnt == 0 {
        return 0
    }
    res := 0
    for len(q) > 0 {
        res++
        nq := [][]int{}
        for i := 0; i < len(q); i++ {
            x, y := q[i][0], q[i][1]
            grid[x][y] = 0
            if x+1 < m && grid[x+1][y] == 1 {
                nq = append(nq, []int{x+1, y})
                grid[x+1][y] -= capacity
            }
            if y+1 < n && grid[x][y+1] == 1 {
                nq = append(nq, []int{x, y+1})
                grid[x][y+1] -= capacity
            }
            if x-1 >= 0 && grid[x-1][y] == 1 {
                nq = append(nq, []int{x-1, y})
                grid[x-1][y] -= capacity
            }
            if y-1 >= 0 && grid[x][y-1] == 1 {
                nq = append(nq, []int{x, y-1})
                grid[x][y-1] -= capacity
            }
        }
        q = nq
    }
    return res
}

// Time:  O(m * n + V * logV + E), V is the number of the source nodes,
//                                , E is the number of the edges
// Space: O(V + E)

// bfs solution
func MaxFill2