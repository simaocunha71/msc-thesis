    freq := make(map[int]int)
    for _, v := range lst {
        freq[v]++
    }
    max := -1
    for k, v := range freq {
        if v >= k {
            if k > max {
                max = k
            }
        }
    }
    return max
}



