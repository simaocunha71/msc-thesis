    result  := make([]int, k)
    n  := len(grid)
    visited  := make([][]bool, n)
    for i := range visited {
        visited[i] = make([]bool, n)
    }

    minPath := math.MaxInt32
    var dfs func(i, j, k int)
    dfs = func(i, j, k int) {
        if k >= minPath {
            return
        }
        if i < 0 || j < 0 || i >= n || j >=