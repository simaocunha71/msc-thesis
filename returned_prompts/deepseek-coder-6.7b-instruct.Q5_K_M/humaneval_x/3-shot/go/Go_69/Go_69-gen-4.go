    m := make(map[int]int)
    max := -1
    for _, v := range lst {
        m[v]++
        if v > max {
            max = v
        }
    }
    for i := max; i >= 1; i-- {
        if m[i] >= i {
            return i
        }
    }
    return -1
}



