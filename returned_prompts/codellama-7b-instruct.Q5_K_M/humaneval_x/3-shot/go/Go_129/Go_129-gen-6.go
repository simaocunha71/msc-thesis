    n := len(grid)
    queue := make([][]int, 0)
    visited := make([][]bool, n)
    for i := 0; i < n; i++ {
        visited[i] = make([]bool, n)
    }

    queue = append(queue, []int{0, 0, 0})
    for len(queue) > 0 {
        current := queue[0]
        queue = queue[1:]
        visited[current[0]][current[1]] = true
        if current[2] == k {
            return current[1:]
        }
        for x, y := current[1]-1, current[2]; x >= 0 && y < k; x, y = x-1, y+1 {
            if visited[current[0]][x] || grid[current[0]][x] > grid[current[0]][current[1]] {
                continue
            }
            queue = append(queue, []int{current[0], x, y})
        }
        for x, y := current[1]+1, current[2]; x < n && y < k; x, y = x+1, y+1 {
            if visited[current[0]][x] || grid[current[0]][x] > grid[current[0]][current[1]] {
                continue
            }
            queue = append(queue, []int{current[0], x, y})
        }
        for y := current[2]+1; y < k; y++ {
            for x := 0; x < n; x++ {
                if visited[x][current[1]] || grid[x][current[1]] > grid[current[0]][current[1]] {
                    continue
                }
                queue = append(queue, []int{x, current[1], y})
            }
        }
    }
    return nil
}



