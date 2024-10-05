    var left_to_right int = 0
    var right_to_left int = 0
    var collision_count int = 0
    for i := 0; i < n; i++ {
        left_to_right += i
        right_to_left += n - i
    }

    for i := 1; i < n; i++ {
        if left_to_right == right_to_left {
            collision_count += 1
            left_to_right += 1
            right_to_left -= 1
        }
    }
    return collision_count
}



