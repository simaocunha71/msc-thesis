    result := 0
    current_capacity := 0

    for _, row := range grid {
        for _, cell := range row {
            current_capacity += cell
            if current_capacity == capacity {
                result += 1
                current_capacity = 0
            } else if current_capacity > capacity {
                result += 1
                current_capacity = current_capacity % capacity
            }
        }
    }
    return result
}



