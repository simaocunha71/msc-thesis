    var freq = make(map[int]int)
    for _, v := range lst {
        freq[v] += 1
    }

    for k, v := range freq {
        if k > 0 && v >= k {
            return k
        }
    }
    return -1
}



