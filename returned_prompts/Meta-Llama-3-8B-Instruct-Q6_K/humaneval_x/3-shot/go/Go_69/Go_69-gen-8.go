    max_freq := 0
    max_num := -1

    for num := range lst {
        freq := 0
        for _, n := range lst {
            if n == num {
                freq += 1
            }
        }
        if freq >= num && freq > max_freq {
            max_freq = freq
            max_num = num
        }
    }

    if max_num == -1 {
        return -1
    }
    return max_num
}