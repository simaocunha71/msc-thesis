    var max_freq int = 0
    var max_val int = 0

    for _, v := range lst {
        freq := 1
        for _, w := range lst {
            if v == w {
                freq += 1
            }
        }
        if freq > max_freq {
            max_freq = freq
            max_val = v
        }
    }

    if max_freq >= max_val {
        return max_val
    } else {
        return -1
    }
}



