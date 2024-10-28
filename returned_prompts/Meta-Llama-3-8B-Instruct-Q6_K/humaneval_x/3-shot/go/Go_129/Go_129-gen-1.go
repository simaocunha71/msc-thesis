    // Create a map to store the grid values and their indices
    valueMap := make(map[int][]struct {
        row, col int
    })
    for i, row := range grid {
        for j, val := range row {
            valueMap[val] = append(valueMap[val], struct {
                row, col int
            }{i, j})
        }
    }

    // Create a map to store the minimum distance from the starting cell
    distMap := make(map[int]int)
    for val, indices := range valueMap {
        distMap[val] = 1 << 31
    }
    distMap[grid[0][0]] = 0

    // Create a map to store the minimum path
    minPath := make(map[int][]int)
    for val, indices := range valueMap {
        minPath[val] = nil
    }
    minPath[grid[0][0]] = []int{grid[0][0]}

    // Dijkstra algorithm
    for val, indices := range valueMap {
        if distMap[val] > k {
            continue
        }
        for _, index := range indices {
            row, col := index.row, index.col
            for dir := 0; dir < 4; dir++ {
                newRow, newCol := row, col
                switch dir {
                case 0: // up
                    newRow -= 1
                case 1: // right
                    newCol += 1
                case 2: // down
                    newRow += 1
                case 3: // left
                    newCol -= 1
                }
                if newRow >= 0 && newRow < len(grid) && newCol >= 0 && newCol < len(grid[0]) {
                    newVal := grid[newRow][newCol]
                    if distMap[newVal] > distMap[val]+1 {
                        distMap[newVal] = distMap[val] + 1
                        minPath[newVal] = append(minPath[val], newVal)
                    }
                }
            }
        }
    }

    // Find the minimum path
    minVal := 1 << 31
    minPathVal := 0
    for val := range distMap {
        if distMap[val] == k {
            if val < minVal {
                minVal = val
                minPathVal = val
            }
        }
    }

    // Return the minimum path
    return minPath