    length := len(arr)
    if length == 0 {
        return 0
    }
    half_length := length / 2
    left_half := arr[:half_length]
    right_half := arr[half_length:]
    left_mirror := make([]int, half_length)
    copy(left_mirror, left_half)
    for i := 0; i < half_length; i++ {
        left_mirror[i] = 1 - left_mirror[i]
    }

    left_changes := 0
    for i := 0; i < half_length; i++ {
        left_changes += int(abs(int(left_half[i]) - left_mirror[i]))
    }

    right_changes := 0
    for i := 0; i < half_length; i++ {
        right_changes += int(abs(int(right_half[i]) - left_mirror[i]))
    }

    return min(left_changes, right_changes)
}



