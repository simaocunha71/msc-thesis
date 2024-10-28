    freq := make(map[int] int)
    for _, v := range lst {
        freq[v] += 1
    }

    for k, v := range freq {
        if v >= k {
            return k
        }
    }
    return -1
}



