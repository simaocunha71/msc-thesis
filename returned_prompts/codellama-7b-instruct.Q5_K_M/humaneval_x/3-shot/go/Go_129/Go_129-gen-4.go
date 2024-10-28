    var result = make([]int, k)
    var current_index = k - 1
    var current_value = 1

    for i := len(grid) - 1; i >= 0; i-- {
        if current_index >= 0 {
            result[current_index] = current_value
            current_index -= 1
        }
        current_value += len(grid)
    }
    return result
}



