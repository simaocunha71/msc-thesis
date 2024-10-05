    var total_collision int = 0
    var left_to_right int = 0
    var right_to_left int = 0

    for i := 1; i < n; i++ {
        if i%2 == 0 {
            left_to_right += 1
            right_to_left += 1
        } else {
            left_to_right += 1
        }
    }

    for i := 1; i < left_to_right; i++ {
        right_to_left -= 1
        total_collision += left_to_right
    }

    return total_collision
}



