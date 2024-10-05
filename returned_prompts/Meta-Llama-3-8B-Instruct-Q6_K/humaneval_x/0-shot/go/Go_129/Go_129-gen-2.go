This problem is a classic example of a shortest path problem, and it can be solved using a depth-first search (DFS) algorithm.

Here is a possible solution in Go:
```go
func Minpath(grid [][]int, k int) []int {
    m, n := len(grid), len(grid[0])
    visited := make([][]bool, m)
    for i := range visited {
        visited[i] = make([]bool, n)
    }
    var res []int
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if dfs(grid, visited, &res, k, i, j) {
                return res
            }
        }
    }
    return nil
}

func dfs(grid [][]int, visited [][]bool, res *[]int, k int, i int, j int) bool {
    m, n := len(grid), len(grid[0])
    if k == 0 {
        *res = append(*res, grid[i][j])
        return true
    }
    if i < 0 || i >= m || j < 0 || j >= n || visited[i][j] {
        return false
    }
    visited[i][j] = true
    for _, neighbor := range [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
        ni, nj := i + neighbor[0], j + neighbor[1]
        if dfs(grid, visited, res, k-1, ni, nj) {
            *res = append(*res, grid[i][j])
            return true
        }
    }
    visited[i][j] = false
    return false
}
```
The `Minpath` function takes a 2D grid and an integer `k` as input, and returns an ordered list of the values on the cells that the minimum path of length `k` goes through.

The `dfs` function is a recursive function that performs a depth-first search of the grid starting from a given cell. It keeps track of the current path and the visited cells, and returns `true` if it finds a path of length `k` that is less than the current minimum path. If it finds a path of length `k` that is not less than the current minimum path, it returns `false`.

The `Minpath` function iterates over