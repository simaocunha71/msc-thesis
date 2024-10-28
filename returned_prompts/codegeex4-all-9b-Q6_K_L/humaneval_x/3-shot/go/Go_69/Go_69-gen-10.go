    result := make(map[int]int)
    max := 0
    for _, v := range lst {
        result[v] += 1
        if result[v] > max {
            max = result[v]
        }
    }
    for k, v := range result {
        if k >= v {
            continue
        } else {
            return k
        }
    }
    return -1
}