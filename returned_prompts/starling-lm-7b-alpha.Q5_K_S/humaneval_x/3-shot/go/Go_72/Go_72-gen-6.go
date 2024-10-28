    if len(q) == 1 {
        if q[0] <= w {
            return true
        }else {
            return false
        }
    }

    left_sum := 0
    right_sum := 0
    for _, qi := range q {
        left_sum += qi
    }
    for i := len(q) - 1; i >= 0; i-- {
        right_sum += q[i]
    }
    if left_sum > right_sum {
        left_sum, right_sum = right_sum, left_sum
    }
    if left_sum + right_sum <= w {
        return true
    }else {
        return false
    }
}



