    result := make(map[int]int)
    var max int = -1

    for _, v := range lst {
        result[v] += 1
    }

    for k, v := range result {
        if k > max && v >= k {
            max = k
        }
    }
    return max
}



