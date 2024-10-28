    half_size := len(arr) / 2
    left := arr[:half_size]
    right := arr[half_size:]
    reverse_right := make([]int, len(right))
    for i, v := range right {
        reverse_right[len(right)-i-1] = v
    }

    left_change := 0
    right_change := 0

    for _, v := range left {
        if v != reverse_right[half_size-left_change-1] {
            left_change += 1
        }
    }
    return left_change + right_change
}



