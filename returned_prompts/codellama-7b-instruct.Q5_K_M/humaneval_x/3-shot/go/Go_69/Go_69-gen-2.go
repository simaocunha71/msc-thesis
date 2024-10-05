    freq := make(map[int]int)
    for _, i := range lst {
        freq[i] += 1
    }

    for i := 1; i < len(lst); i++ {
        if freq[i] >= i {
            return i
        }
    }
    return -1
}



