    var n int = len(grid)
    var memo map[[2]int][]int
    memo = make(map[[2]int][]int)

    func dfs(x, y int, k int, path []int) []int {
        if k == 0 {
            return path
        }
        var key [2]int
        key[0] = x
        key[1] = y
        if val, ok := memo[key]; ok {
            return val
        }
        var res []int
        for _, dx := range []int{-1, 0, 1} {
            for _, dy := range []int{-1, 0, 1} {
                nx, ny := x+dx, y+dy
                if nx >= 0 && nx < n && ny >= 0 && ny < n {
                    res = append(res, dfs(nx, ny, k-1, append(path, grid[nx][ny])))
                }
            }
        }
        memo[key] = res
        return res
    }

    var res []int
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            res = append(res, dfs(i, j, k, []int{grid[i][j]}))
        }
    }
    sort.Slice(res, func(i, j int) bool {
        return less(res[i], res[j])
    })
    return res[0]

    func less(a, b []int) bool {
        for i := 0; i < len(a) && i < len(b); i++ {
            if a[i] < b[i] {
                return true
            }
            if a[i] > b[i] {
                return false
            }
        }
        return len(a) < len(b)
    }
}
}