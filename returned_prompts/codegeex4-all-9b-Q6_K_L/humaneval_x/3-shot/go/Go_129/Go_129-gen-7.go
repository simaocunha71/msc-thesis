    result := make([]int, 0)
    queue := make([][]int, 0)
    visited := make(map[[2]int]bool)

    start := [2]int{0,0}
    queue = append(queue, start)
    visited[start] = true

    for len(queue) != 0 {
        current := queue[0]
        queue = queue[1:]

        if len(result) == k {
            break
        }

        result = append(result, grid[current[0]][current[1]])
        neighbors := getNeighbors(grid, current)
        for _, n := range neighbors {
            if !visited[n] {
                visited[n] = true
                queue = append(queue, n)
            }
        }
    }
    return result
}

func getNeighbors(grid [][]int, cell [2]int) [][2]int {
    result := make([][2]int, 0)
    neighbors := [4][2]int{
        {cell[0]-1, cell[1]},
        {cell[0]+1, cell[1]},
        {cell[0], cell[1]-1},
        {cell[0], cell[1]+1},
    }
    for _, n := range neighbors {
        if n[0] >= 0 && n[0] < len(grid) && n[1] >= 0 && n[1] < len(grid[0]) {
            result = append(result, n)
        }
    }
    return result
}



