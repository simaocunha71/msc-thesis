    var max_fill = 0
    var current_fill = 0
    var current_row = 0

    for current_row < len(grid) {
        current_fill = 0
        for _, c := range grid[current_row] {
            if c == 1 {
                current_fill += 1
            }
        }
        max_fill = math.Max(max_fill, current_fill)
        current_row += 1
    }

    return max_fill
}



