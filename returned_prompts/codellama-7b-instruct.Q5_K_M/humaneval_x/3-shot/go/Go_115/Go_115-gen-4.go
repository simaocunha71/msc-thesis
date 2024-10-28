    var max_row, max_col int
    var current_row, current_col int
    var result int

    for row := 0; row < len(grid); row++ {
        for col := 0; col < len(grid[0]); col++ {
            if grid[row][col] == 1{
                max_row = row
                max_col = col
            }
        }
    }

    current_row = max_row
    current_col = max_col

    for current_row > -1 && current_col > -1 {
        if current_row == 0 && current_col == 0 {
            break
        }
        if current_row > 0 && current_col > 0 && grid[current_row - 1][current_col - 1] == 1 {
            current_row -= 1
            current_col -= 1
            result += 1
        } else if current_row > 0 && grid[current_row - 1][current_col] == 1 {
            current_row -= 1
            result += 1
        } else if current_col > 0 && grid[current_row][current_col - 1] == 1 {
            current_col -= 1
            result += 1
        } else {
            break
        }
    }

    return result
}



