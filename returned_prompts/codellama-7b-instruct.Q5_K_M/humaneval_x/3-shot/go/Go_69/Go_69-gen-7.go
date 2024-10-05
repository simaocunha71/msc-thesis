    var max_freq = 0
    var max_val = 0

    for _, i := range lst {
        freq := 0
        for _, j := range lst {
            if i == j {
                freq += 1
            }
        }

        if freq > max_freq {
            max_freq = freq
            max_val = i
        }
    }

    if max_freq >= max_val {
        return max_val
    }

    return -1
}



