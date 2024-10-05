    var max_neg int
    var min_pos int

    for _, n := range lst {
        if n < 0 {
            if max_neg == 0 || n > max_neg {
                max_neg = n
            }
        } else if n > 0 {
            if min_pos == 0 || n < min_pos {
                min_pos = n
            }
        }
    }

    return [2]interface{}{max_neg, min_pos}
}



