    result  := make([]int, k)
    n  := len(grid)
    visited  := make([][]bool, n)
    for i  := range visited  {
        visited[i] =  make([]bool, n)
    }

    var dfs func(i, j, k int)
    dfs =  func(i, j, k int)  {
        if k  != 0  {
            result[len(result)  - k] =  grid[i][j]
        }
        if k  != 1  {
            visited[i][j] =  true
            dirs  :=  [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
            tmp  :=  make([]int, 0)
            for _, dir  := range dirs  {
                ni, nj  :=  i + dir[0], j + dir[1]
                if ni  >= 0  && ni < n  && nj  >= 0  && nj < n  && !visited[ni][nj]  {
                    tmp =  append(tmp, grid[ni][nj])
                }
            }
            sort.Ints(tmp)
            for _, v  := range tmp  {
                for ii, jj, found  := range visited  {
                    for jjj, vv  := range found  {
                        if vv  && grid[ii][jjj]  != v  {
                            dfs(ii, jjj, k - 1)
                            return
                        }
                    }
                }
            }
            visited[i][j] =  false
        }
    }

    for i, found  := range visited  {
        for j, vv  := range found  {
            if !vv  {
                dfs(i, j, k)
                return result
            }
        }
    }

    return result
}



