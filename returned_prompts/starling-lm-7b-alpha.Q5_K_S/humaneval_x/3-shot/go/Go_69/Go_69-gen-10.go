    freq := make(map[int]int)
    for _, i := range lst {
        freq[i] += 1
    }
    for i := len(lst); i > 0; i-- {
        if freq[i] >= i {
            return i
        }
    }
    return -1
}



