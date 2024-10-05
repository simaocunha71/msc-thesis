    frequencies := make(map[int]int)
    for _, v := range lst {
        frequencies[v]++
    }

    for k, v := range frequencies {
        if v >= k {
            return k
        }
    }

    return -1
}



