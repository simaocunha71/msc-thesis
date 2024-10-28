    m := make(map[int]int)
    for _, val := range lst {
        m[val]++
    }
    for key := range m {
        if key >= m[key] {
            return key
        }
    }
    return -1
}



