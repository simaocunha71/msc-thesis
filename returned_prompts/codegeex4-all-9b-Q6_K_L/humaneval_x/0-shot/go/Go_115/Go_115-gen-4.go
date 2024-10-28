```go
func MaxFill(grid [][]int, capacity int) int {
    n, m := len(grid), len(grid[0])
    res := 0
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] == 1 {
                res += int(math.Ceil(float64(capacity) / float64(m)))
            }
        }
    }
    return res
}
```
B:
```go
func MaxFill(grid [][]int, capacity int) int {
    n, m := len(grid), len(grid[0])
    res := 0
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] == 1 {
                res += int(math.Ceil(float64(capacity) / float64(n)))
            }
        }
    }
    return res
}
```
C:
```go
func MaxFill(grid [][]int, capacity int) int {
    n, m := len(grid), len(grid[0])
    res := 0
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] == 1 {
                res += int(math.Ceil(float64(capacity) / float64(n*m)))
            }
        }
    }
    return res
}
```
D:
```go
func MaxFill(grid [][]int, capacity int) int {
    n, m := len(grid), len(grid[0])
    res := 0
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] == 1 {
                res += int(math.Ceil(float64(capacity) / float64(grid[i][j])))
            }
        }
    }
    return res
}
```
E:
```go
func MaxFill(grid [][]int, capacity int) int {
    n, m := len(grid), len(grid[0])
    res := 0
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if grid[i][j] == 1 {
                res += int(math.Ceil(float64(capacity) / float64