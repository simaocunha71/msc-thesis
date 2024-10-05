    n := len(grid)
    result := make([]int, 0)
    queue := make([]*struct {
        x, y int
        path []int
    }, 0)

    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            queue = append(queue, &struct {
                x, y int
                path []int
            }{x: i, y: j, path: []int{grid[i][j]}})
        }
    }

    for len(queue) > 0 {
        q := queue[0]
        queue = queue[1:]

        if len(q.path) == k {
            if len(result) == 0 || q.path < result[len(result)-1] {
                result = q.path
            }
            continue
        }

        if q.x > 0 {
            queue = append(queue, &struct {
                x, y int
                path []int
            }{x: q.x - 1, y: q.y, path: append([]int{}, q.path...)})
        }
        if q.x < n - 1 {
            queue = append(queue, &struct {
                x, y int
                path []int
            }{x: q.x + 1, y: q.y, path: append([]int{}, q.path...)})
        }
        if q.y > 0 {
            queue = append(queue, &struct {
                x, y int
                path []int
            }{x: q.x, y: q.y - 1, path: append([]int{}, q.path...)})
        }
        if q.y < n - 1 {
            queue = append(queue, &struct {
                x, y int
                path []int
            }{x: q.x, y: q.y + 1, path: append([]int{}, q.path...)})
        }
    }

    return result
}