    count := make(map[int]int)
    for _, v := range lst {
        count[v]++
    }
    for k, v := range count {
        if v >= k {
            return k
        }
    }
    return -1
}



