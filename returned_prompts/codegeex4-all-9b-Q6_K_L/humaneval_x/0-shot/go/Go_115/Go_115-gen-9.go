```go
func MaxFill(grid [][]int, capacity int) int {
    count := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] == 1 {
                count += 1
            }
        }
    }
    return count / capacity
}
```
B:
```go
func MaxFill(grid [][]int, capacity int) int {
    count := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] == 1 {
                count += 1
            }
        }
    }
    return count % capacity
}
```
C:
```go
func MaxFill(grid [][]int, capacity int) int {
    count := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] == 1 {
                count += 1
            }
        }
    }
    return count / capacity + count % capacity
}
```
D:
```go
func MaxFill(grid [][]int, capacity int) int {
    count := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] == 1 {
                count += 1
            }
        }
    }
    return math.Ceil(float64(count) / float64(capacity))
}
```

E:
```go
func MaxFill(grid [][]int, capacity int) int {
    count := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] == 1 {
                count += 1
            }
        }
    }
    return count / capacity * capacity
}
```

F:
```go
func MaxFill(grid [][]int, capacity int) int {
    count := 0
    for i := 0; i < len(grid); i++ {
        for j := 0; j < len(grid[i]); j++ {
            if grid[i][j] == 1 {
                count += 